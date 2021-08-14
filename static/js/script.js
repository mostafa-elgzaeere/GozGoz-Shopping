// let quantity=document.getElementById("quantity"),
//     plus=document.getElementsByClassName("plus-btn"),
//     minus=document.getElementsByClassName("minus-btn"),
//     price=document.getElementsByClassName("total-price"),
//     total=document.getElementById("total"),
//     all_prices=document.getElementById("all_prices");
//     all_prices.textContent=total.textContent;

// for ( var counter = 0; counter < plus.length; counter++){
//     plus[counter].onclick=()=>{
//     x=parseInt(quantity.value)
//     quantity.value= x+1

//     total.textContent=quantity.value*price[counter].textContent+"$";
//     all_prices.textContent=total.textContent
// }
// }    


// for ( var counter = 0; counter < minus.length; counter++){
//     minus[counter].onclick=()=>{
//         if (quantity.value>0){
//             x=parseInt(quantity.value)
//             quantity.value= x-1
//             total.textContent=quantity.value*price[counter].textContent+"$";
//     }
// }
// }   

// $('.minus-btn').on('click', function(e) {
//     e.preventDefault();
//     var $this = $(this);
//     var $input = $this.closest('div').find('input');
//     var value = parseInt($input.val());


 
//     if (value){
//         value = value - 1;
//     } 
//     else {
//         value = 0;
//     }
 
//   $input.val(value);
 
// });
 
// $('.plus-btn').on('click', function(e) {
//     e.preventDefault();
//     var $this = $(this);
//     var $input = $this.closest('div').find('input');
//     var value = parseInt($input.val());
 
//     if (value) {
//         value = value + 1;
//     } else {
//         value =100;
//     }
 
//     $input.val(value);
// });