var publish_modal = document.getElementById('publish_modal');
publish_modal.addEventListener("show.bs.modal",function(event){
    var button = event.relatedTarget;
    var product_name=button.getAttribute('data-name');
    var product_total_quantity=button.getAttribute('data-quantity');
    var id_product=button.getAttribute('data-id');
    console.log("Product ID:" ,id_product)
    var product_total_sale_price=button.getAttribute('data-price');
    var modal_title = publish_modal.querySelector('.modal-title');
    var modal_attribute_quantity = publish_modal.querySelector("#quantity");
    var modal_id_product = publish_modal.querySelector("#id_product");
    modal_title.textContent= "ID: " + id_product + "      " + product_name;
    modal_attribute_quantity.setAttribute("max",product_total_quantity);
    modal_id_product.value = id_product;
})