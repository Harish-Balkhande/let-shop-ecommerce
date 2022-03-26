$('#slider1, #slider2, #slider3, #slider4').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


// To show Increase quantity of product in cart on '+' click
$('.plus-cart').click(function (){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log(qnt);
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function (data){
            console.log(data)
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("total_amt").innerText = data.total;
        }
    })
})

// To show decreade quantity of product in cart on '-' click
$('.minus-cart').click(function (){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log(qnt);
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function (data){
            // console.log(data)
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("total_amt").innerText = data.total;
        }
    })
})

// Remove product in cart
$('.remove-item').click(function (){
    var id = $(this).attr("pid").toString();
    var prod = this    
    $.ajax({
        type:"GET",
        url:"/removeitem",
        data:{
            prod_id:id
        },
        success:function (data){            
            prod.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("total_amt").innerText = data.total;
            prod.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})

// show number of product in cart (cart banner)
$(document).ready(function(){        
    $.get("cartbadge/", function(data){        
        var txt = "<span class=\"badge bg-danger\" >"+ data.badge +"</span>Cart"
        if (data.badge != 0){
            document.getElementById("cart-badge").innerHTML = txt
        }        
    })    
})
