(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach( function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');

      thisForm.querySelector('.loading').classList.add('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');
      thisForm.querySelector('.error-message').classList.remove('d-block');

      let formData = new FormData(thisForm);

      php_email_form_submit(thisForm, action, formData);
    });
  });

  function php_email_form_submit(thisForm, action, formData) {
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

})();
