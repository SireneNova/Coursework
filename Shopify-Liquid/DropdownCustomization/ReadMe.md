
# Add "Pick an option" choice to product selection lists
By default, product selection dropdown menus dont have empty, "-select-" options, which would be convenient in certain circumstances, such as when you are clicking an image rather thn the menu to select a product. As described [here](https://github.com/rebeccapizano/Coursework/tree/master/Shopify-Liquid/ClickImageToSelectProduct), some product variants have the same image, like different sizes of a shirt, so it would be helpful to have a default selection like "pick a size" so that a dropdown update doesn't neccessarily assume only one possibility out of multiple when an image is first clicked (like showing a size default of small).
___
## Objective
Add default "pick an option" label to dropdown menus. 

## Steps Taken
Tried adding something like ```<option>-select-<option>``` to the product page template code, but nothing changed. Found documentation on how to do this [here](https://help.shopify.com/en/themes/customization/products/variants/how-to-add-a-pick-an-option-to-drop-downs#non-sectioned-themes). Followed the steps for non-sectioned themes:

* Added a "pick an option snippet", which creates the option and custom label.
```
{% comment %}
  See https://docs.shopify.com/themes/customization/products/how-to-add-a-pick-an-option-to-drop-downs
{% endcomment %}

{% unless product.selected_variant %}
  {% if product.variants.size > 1 %}
    <script>
    var $addToCartForm = $('form[action="/cart/add"]');
    if (window.MutationObserver && $addToCartForm.length) {
      if (typeof observer === 'object' && typeof observer.disconnect === 'function') {
        observer.disconnect();
      }
      var config = { childList: true, subtree: true };
      var observer = new MutationObserver(function() {      
        {% for option in product.options %}
          $('.single-option-selector:eq({{ forloop.index0 }})')
            .filter(function() { 
              return $(this).find('option').size() > 1  
            })
            .prepend('<option value="">Pick a ' + {{ product.options[forloop.index0] | json }} + '</option>')
            .val('')
            .trigger('change');
        {% endfor %}
        observer.disconnect();
      });  
      observer.observe($addToCartForm[0], config);
    } 
    </script>  
  {% endif %}
{% endunless %}
```
* Included the snippet by entering ```{% include 'pick-an-option' %}``` in the body of theme.liquid.
* Replaced existing option code in product.liquid, which accommodated the new selection by checking the length of a loop. Replaced this -
```		
<option  {% if variant == current_variant %} selected="selected" {% endif %} 
data-sku="{{ variant.sku }}" 
value="{{ variant.id }}" 
{% unless variant.available %} disabled="disabled" {% endunless %}>
{% if variant.available %} {{ variant.title }} - {{ variant.price | money_with_currency }}
{% else %} {{ variant.title }} - {{ 'products.product.sold_out' | t }} {% endif %}' </option>
```
With this, which also appears to simplify other existing code at the end- 
```
<option {% if forloop.length <= 1 and variant==product.selected_or_first_available_variant %} selected="selected" {% endif %} 
data-sku="{{ variant.sku }}" 
value="{{ variant.id }}">{{ variant.title }} - {{ variant.price | money_with_currency }}</option>
```
* Changed the language settings so that the "add to cart" button shows as "make a selection" instead of "unavailable", to accomodate the new options. It also shows this when a user selects any combination that doesn't exist, which makes more sense. It was found by searching "unavailable" in "filter translations".


## Results
It was far more complex to achieve this change than expected in Liquid, but it works beautifully, and the documentation was easy to find and follow. I had thought The next step is to attempt to disable options that don't exist after another option is selected.

Here is the final result:
![alt text](https://github.com/rebeccapizano/Coursework/blob/master/Shopify-Liquid/DropdownCustomization/solvedPickAnOption.png)
