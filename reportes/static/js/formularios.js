jQuery.validator.setDefaults({
  errorElement : 'div',
  errorClass:'error red-text',
  errorPlacement: function(error, element) {
    var placement = $(element).data('error');
    if (placement) {
      $(placement).append(error)
    } else {
      error.insertAfter(element);
    }
  }
});

$.validator.addMethod(
  "regex",
  function(value, element, regexp) {
    var check = false;
    var re = new RegExp(regexp);
    return this.optional(element) || re.test(value);
  },""
);

$("form").not(".sin_validar").validate();
