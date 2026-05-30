class Ingredient:
    def __init(self, name: str):
        self.name = name
    
    def __eq__(self, other):
        return isistance(other, Ingredient) and self.name == other.name
        
    def __hash__(self):
        return hash(self.name)
        
    
class Recipe:
    def __init__(self, name:str, ingredients: list[str]):
        self.name =name
        self.ingredients = set(Ingredient(ing) for ing in ingredients)
    
    def __repr__(self):
        return self.name

class RecipeStore:
    def __init__(self):
        self.recipes = []
        self.index = {}
    
    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)
        
        for ingredient in recipe.ingredients:
            if ingredient not in self.index:
                self.index[ingredient] = set()
            self.index[ingredient].add(recipe)
            
    def search_by_ingredient(self, ingredient_name: str) -> list[Recipe]:
        
        ingredient = Ingredient(ingredient_name)
        
        return list(self.index.get(ingredient, []))