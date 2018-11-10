# Click Image to Select Product
On product pages, there is a list of product images, which includes different variants, as well as dropdown lists from which to make a selection. The dropdowns correspond to different options (size, color, style, etc.). Making a selection from the dropdown changes the featured image to the matching variant image. However by default, the reverse isn't true. Clicking the images changes the featured image, but does not change the dropdown selection. For products with a lot of variants, this makes it difficult to identify the selection to make if you see an image you like. It could even lead a customer to add the wrong variant to cart if they assume an updated image matches a non-matching dropdown selection. How annoying would that be!
___
## Objective
The goal was to change the default product page code to allow a matching dropdown selection to show up when a product image is clicked. Here is an image summarizing the problem and desired function:
![alt text](https://github.com/rebeccapizano/Coursework/blob/master/Shopify-Liquid/ClickImageToSelectProduct/DropdownDescription.png)

## Steps Taken
Since some product variants have the same image, like different sizes of a shirt, the new design would benefit from having a default selection like "pick a size" so that a dropdown update doesn't neccessarily assume a size when an image is clicked. This dropdown customization was done [here](https://github.com/rebeccapizano/Coursework/tree/master/Shopify-Liquid/DropdownCustomization).

I attempted to change the code by observing it, but the structure was too unfamiliar to get the result. I did become more familiar with general ways to make JavaScript changes. 

I discovered an online course in Liquid through Lynda and after wathcing a lesson, realizd that Shopify has good documentation, and to check it out. I then found documentation on Shopify that explained exactly how to [Select a variant by clicking on its image](https://help.shopify.com/en/themes/customization/products/variants/select-variants-by-clicking-images). 

The additions made were very complex: 

For my theme, this needed to be placed in theme.liquid rather than product.liquid:
```
{% comment %}
Place this in your product.liquid template, at the bottom.
{% endcomment %}
{% if product.variants.size > 1 %}
<script>
  var variantImages = {},
    thumbnails,
    variant,
    variantImage,
    optionValue,
    productOptions = [];
    {% for variant in product.variants %}
       variant = {{ variant | json }};
       if ( typeof variant.featured_image !== 'undefined' && variant.featured_image !== null ) {
         variantImage =  variant.featured_image.src.split('?')[0].replace(/http(s)?:/,'');
         variantImages[variantImage] = variantImages[variantImage] || {};
         {% for option in product.options %}
         
           {% assign option_value = variant.options[forloop.index0] %}
           {% assign option_key = 'option-' | append: forloop.index0 %}
         	
           if (typeof variantImages[variantImage][{{ option_key | json }}] === 'undefined') {
             variantImages[variantImage][{{ option_key | json }}] = {{ option_value | json }};
           }
           else {
             var oldValue = variantImages[variantImage][{{ option_key | json }}];
             if ( oldValue !== null && oldValue !== {{ option_value | json }} )  {
               variantImages[variantImage][{{ option_key | json }}] = null;
             }
           }
         {% endfor %}
       }
       productOptions.push(variant);
    {% endfor %}
</script> 
{% endif %}
```
This was places in theme.liquid.js:
```
$(document).ready(function() {
  thumbnails = $('img[src*="/products/"]').not(':first');
  if (thumbnails.length) {
    thumbnails.bind('click', function() {
      var arrImage = $(this).attr('src').split('?')[0].split('.');
      var strExtention = arrImage.pop();
      var strRemaining = arrImage.pop().replace(/_[a-zA-Z0-9@]+$/,'');
      var strNewImage = arrImage.join('.')+"."+strRemaining+"."+strExtention;
      if (typeof variantImages[strNewImage] !== 'undefined') {
          productOptions.forEach(function (value, i) {
           optionValue = variantImages[strNewImage]['option-'+i];
           if (optionValue !== null && $('.single-option-selector:eq('+i+') option').filter(function() { return $(this).text() === optionValue }).length) {
             $('.single-option-selector:eq('+i+')').val(optionValue).trigger('change');
           }
        });
      }
    });
  }
});
```

## Results

