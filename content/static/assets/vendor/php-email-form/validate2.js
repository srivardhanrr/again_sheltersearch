(function () {
  "use strict";

  let forms = document.querySelectorAll('.register-payment');

  forms.forEach( function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');

      thisForm.querySelector('.loading').classList.add('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');
      thisForm.querySelector('.error-message').classList.remove('d-block');

      let formData = new FormData(thisForm);
      let name = formData.get("name");
      let phone = formData.get("phone");
      let email = formData.get("email");
      let order_id = formData.get("order_id");

      php_email_form_submit(thisForm, action, formData, name, phone, email, order_id);
    });
  });

  function form_save(thisForm, action, formData) {
      fetch(action, {
      method: 'POST',
      body: formData,
      headers: {'X-Requested-With': 'XMLHttpRequest'}
    }).then(response => {
      return response.text();
    }).then(data => {
      thisForm.querySelector('.loading').classList.remove('d-block');
      thisForm.querySelector('.sent-message').classList.add('d-block');
      thisForm.reset();
    });
  }

  function php_email_form_submit(thisForm, action, formData, name, phone, email, order_id) {
    let options =
                {
                    "key": "rzp_test_OIqW58d6nL7eHG",
                    "name": "ShelterSearch",
                    "description": "ShelterSearch",
                    "image": "https://sheltersearch.in/static/assets/img/logo4.png",
                    "order_id": order_id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                    // "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
                    "handler": function (response){
                            formData.set("pay_id", response.razorpay_payment_id);
                            formData.set("paid", "Yes");
                            formData.set("signature", response.razorpay_signature);
                            form_save(thisForm, action, formData)},
                    "prefill": {
                        "name": name, //your customer's name
                        "email": email,
                        "contact": phone
                    },
                    "notes": {
                        "address": "Bengaluru"
                    },
                    "theme": {
                        "color": "#3399cc"
                    }
                };
    let rzp1 = new Razorpay(options);
    rzp1.open();
  }

})();
