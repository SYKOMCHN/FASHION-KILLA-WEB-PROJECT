document.addEventListener("click", function (e) {

  const card = e.target.closest(".item-card");
  if (!card) return;
  if (e.target.closest("button")) return; // ignore other button clicks

  const id = card.dataset.id || card.querySelector(".add-to-cart")?.dataset.id || "";
  const img = card.querySelector(".item-img img")?.src || "/assets/extras/yessir.png";
  const name = card.querySelector(".item-name")?.textContent?.trim() || "";
  const priceText = card.querySelector(".item-price")?.textContent?.trim() || "";
  const desc = card.querySelector(".item-desc")?.textContent?.trim() || "No description.";

  // build overlay template then populate
  const overlay = document.createElement("div");
  overlay.className = "popup-overlay";
  overlay.innerHTML = `
    <div class="popup" role="dialog" aria-modal="true">
      <button class="popup-close">&times;</button>
      <div class="popup-left">
        <div class="popup-img"><img class="popup-img-el" src="" alt=""></div>
        <div class="popup-name"></div>
        <div class="popup-price"></div>
      </div>
      <div class="popup-right">
        <div class="popup-desc"></div>
        <div class="popup-actions">
          <button class="popup-add">Add to cart</button>
        </div>
      </div>
    </div>
  `;

  // populate data
  overlay.querySelector(".popup-img-el").src = img;
  overlay.querySelector(".popup-img-el").alt = name || "Product";
  overlay.querySelector(".popup-name").textContent = name;
  overlay.querySelector(".popup-price").textContent = priceText;
  overlay.querySelector(".popup-desc").textContent = desc;

  // make buttons work!!!
  overlay.querySelector(".popup-close").addEventListener("click", () => overlay.remove());

    overlay.querySelector(".popup-add").addEventListener("click", function () {
        const btn = this;
        console.log("Add to cart (popup):", id);

        fetch("/add_to_cart/" + id, { method: "POST" })
            .then(() => {
            btn.textContent = "Added ✓";
            // update the open cart dropdown if it's visible
            if (window.refreshCart) window.refreshCart();
            setTimeout(() => (btn.textContent = "Add to cart"), 900);
        });

    });





  // clicking outside popup closes it
  overlay.addEventListener("click", (ev) => {
    if (ev.target === overlay) overlay.remove();
  });

  document.body.appendChild(overlay);
});


document.querySelectorAll(".add-to-cart").forEach(btn => {
  btn.addEventListener("click", function () {
    const id = this.dataset.id;
    fetch("/add_to_cart/" + id, { method: "POST" })
      .then(() => {
        this.innerHTML = `<i class="fa-solid fa-cart-shopping"></i> Added ✓`;
        // update the open cart dropdown if visible
        if (window.refreshCart) window.refreshCart();
        setTimeout(() => this.innerHTML = `<i class="fa-solid fa-cart-shopping"></i> Add to cart`, 900);
      });
  });
});


// handler for any add-to-cart button
document.body.addEventListener("click", function (e) {
  const btn = e.target.closest(".add-to-cart");
  if (!btn) return;

  // prevent duplicate clicks
  e.preventDefault();
  const id = btn.dataset.id;
  if (!id) return;

  const previous = btn.innerHTML;
  btn.innerHTML = "Added ✓";

  fetch("/add_to_cart/" + id, { method: "POST" })
    .then(() => {
      // update open dropdown/cart
      if (window.refreshCart) window.refreshCart();
      setTimeout(() => {
        // restore button
        btn.innerHTML = previous;
      }, 900);
    })
    .catch(() => {
      // on error, restore button
      btn.innerHTML = previous;
    });
});
