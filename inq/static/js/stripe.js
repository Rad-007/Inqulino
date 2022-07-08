


var createCheckoutSession=function(priceld){
    return fetch("/create-checkout-session",{
      method: "POST",
       headers:{
         "Content-Type": "application/json"
       },
       body: JSON. stringify({
        priceid: priceid
       })
    }). then(function(result){
       return result.json();
       });
    };

const lend= "price_1Kw2jsSH9T6h17WB05BxhCwK";

const stripe=Stripe("pk_test_51Kw2h5SH9T6h17WBpVYjECW0ipM2p3WLHA40dl1MXVXoff32EEu2CRTZt863GZTA1nL3XSGgAgq5aMq9NXJZmFVP00BYnNcYi6");

//const BASIC_PRICE_ID="price_iItbEhIQ25ykYZINT=QOnrRh";

document. addEventlistener("DOMContentloaded", function(event){
  document
  .getElementById("stripe")
  .addEventlistener ("click", function(evt){
   });
});


document.addEventListener('DOMContentLoaded', async () => {
  let searchParams = new URLSearchParams(window.location.search);
  if (searchParams.has('session_id')) {
    const session_id = searchParams.get('session_id');
    document.getElementById('session-id').setAttribute('value', session_id);
  }
});