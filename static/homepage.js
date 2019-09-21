var ingredients = [
  "romaine lettuce",
    "Black Olives", "Grape Tomatoes","Garlic","Pepper",
    "Purple Onion",
    "Seasoning",
    "Garbanzo Beans",
    "Feta Cheese Crumbles",
    "Plain Flour",
    "Ground Pepper",
    "Salt",
    "Tomatoes",
    "Ground Black Pepper",
    "Thyme",
    "Eggs",
    "Green Tomatoes",
    "Yellow Corn Meal",
    "Milk",
    "Vegetable Oil", "Chicken Broth",
    "Parsley",
    "Dried Basil",
    "Garlic",
    "Bone in Chicken Thighs",
    "Pasta",
    "Olive Oil",
    "Crushed Red Pepper",
    "Crushed Tomatoes",
    "Diced Tomatoes",
    "All-Purpose Flour",
    "Pepper",
    "Butter",
    "Dry white wine",
    "White wine vinegar",
    "Lemon zest",
    "Fresh tarragon",
    "Shallots"
];
function getMatches()
{
  var query = document.getElementById('myInput').value;
  var holder = 0;
  for(var i = 0; i < ingredients.length; i++)
  {
    if(ingredients[i].substring(0,query.length) == query)
    {
      holder = i;
      break;
    }
  }

  console.log(ingredients[i]);

}

function loadData(data)
{
    ingredients = data;
}

$('#autocomplete').autocomplete({
  // serviceUrl: '/autosuggest/service/url',
  // lookup: countriesString,
  source: ingredients,
  lookup: ingredients,
  lookupFilter: function(suggestion, originalQuery, queryLowerCase) {
      var re = new RegExp('\\b' + $.Autocomplete.utils.escapeRegExChars(queryLowerCase), 'gi');
      return re.test(suggestion.value);
  },
  onSelect: function(suggestion) {
      $('#selction-ajax').html('You selected: ' + suggestion.value + ', ' + suggestion.data);
  },
  onHint: function (hint) {
      $('#autocomplete-ajax-x').val(hint);
  },
  onInvalidateSelection: function() {
      $('#selction-ajax').html('You selected: none');
  }
});