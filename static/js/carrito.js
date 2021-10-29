console.log('🐼')
const addCart = document.querySelectorAll('.addCart');

addCart.forEach((addCartButton) => {
    addCartButton.addEventListener('click', addToCartClicked);
});

const comprarButton = document.querySelector('.comprarButton');
comprarButton.addEventListener('click', comprarButtonClicked)

const shoppingCartItemsContainer = document.querySelector(
    '.shoppingCartItemsContainer'
);

function addToCartClicked(event) {
    const button = event.target;
    const card = button.closest('.card');
    
    const cardTitle = card.querySelector('.card-text').textContent;
    const cardPrice = card.querySelector('.card-link').textContent;
    const cardImage = card.querySelector('.card-img-top').src;
    
    addCardToShoppingCard(cardTitle, cardPrice, cardImage)
}

function addCardToShoppingCard(cardTitle, cardPrice, cardImage) {
    const elementsTitle = shoppingCartItemsContainer.getElementsByClassName(
        'shoppingCartItemTitle'
    );
    for(let i = 0; i < elementsTitle.length; i++){
        if (elementsTitle[i].innerText === cardTitle){
            let elementQuantity = elementsTitle[i].parentElement.parentElement.parentElement.
            querySelector('.shoppingCartItemQuantity');
        elementQuantity.value++;
        $('.toast').toast('show');
        updateShoppingCartTotal();
        return;        
        }
    }

    const shoppingCartRow = document.createElement('div');
    const shoppingCartContent = `
    <div class="row shoppingCartItem">
        <div class="col-6">
            <div class="shopping-cart-item d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                <img src=${cardImage} class="shopping-cart-image">
                <h6 class="shopping-cart-item-title shoppingCartItemTitle text-truncate ml-3 mb-0">${cardTitle}</h6>
            </div>
        </div>
        <div class="col-2">
            <div class="shopping-cart-price d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                <p class="item-price mb-0 shoppingCartItemPrice">${cardPrice}</p>
            </div>
        </div>
        <div class="col-4">
            <div
                class="shopping-cart-quantity d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">
                <input class="shopping-cart-quantity-input shoppingCartItemQuantity" type="number"
                    value="1">
                <button class="btn btn-danger buttonDelete" type="button">X</button>
            </div>
        </div>
    </div>`;
    shoppingCartRow.innerHTML = shoppingCartContent
    shoppingCartItemsContainer.append(shoppingCartRow);

    shoppingCartRow.querySelector('.buttonDelete')
    .addEventListener('click', removeShoppingCartItem);

    shoppingCartRow.querySelector('.shoppingCartItemQuantity').
    addEventListener('change', quantityChanged)

    updateShoppingCartTotal()
}

function updateShoppingCartTotal() {
    let total = 0;
    const shoppingCartTotal = document.querySelector('.shoppingCartTotal');

    const shoppingCartItems = document.querySelectorAll('.shoppingCartItem');

    shoppingCartItems.forEach((shoppingCartItem) => {
        const shoppingCartItemPriceElement = shoppingCartItem.querySelector(
            '.shoppingCartItemPrice'
            );
        
        const shoppingCartItemPrice = Number(shoppingCartItemPriceElement.textContent.
        replace(
            '$',
            '')
        );
        const shoppingCartItemQuantityElement = shoppingCartItem.querySelector('.shoppingCartItemQuantity');
        
        const shoppingCartItemQuantity = Number(shoppingCartItemQuantityElement.value);
        
        total = total + shoppingCartItemPrice * shoppingCartItemQuantity;
        
        console.log(
            'updateShoppingCartTotal -> total',
            total);   
          
    });
    shoppingCartTotal.innerHTML = `${total.toFixed(2)}$`;

}

function removeShoppingCartItem(event) {
    const buttonClicked = event.target;
    buttonClicked.closest('.shoppingCartItem').remove();
    updateShoppingCartTotal();
}

function quantityChanged(event) {
    const input = event.target;
    if (input.value<=0) {
        input.value = 1
    }
    updateShoppingCartTotal();
}

function comprarButtonClicked() {
    shoppingCartItemsContainer.innerHTML = '';
    updateShoppingCartTotal();
}




