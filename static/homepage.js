var ingredients = []
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
