def main():
# TODO: Step 2 - Create a complex data structure
    about_me = {
                'full_name' : 'Devendra Sagar', 
                'student_id' : 10309161,
                'pizza_toppings' : [
                    'bacon' ,
                    'Cheese' ,
                    'pinapple'
                ],
                'movies' : [
                    {'title' : 'Its a wonderful Life',
                    'genre' : 'Drama'},
                    {'title' : 'Hackers',
                    'genre' : 'Nerd Action'},
                ] 

    }
    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title' : 'Stars Wars',
                               'genre' : 'Sci-Fi'})
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
   
    about_me = add_pizza_toppings(about_me, ('Paneer', 'Tomato', 'Mushrooms', 'Green Cilli'))
    print_pizza_toppings(about_me)
   
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])

    return


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(data_struct):
    full_name = data_struct['full_name']
    first_name = (full_name.split(' '))[0]
    student_id = data_struct['student_id']

    print(f'My name is {full_name}, but you call me sir {first_name}.')
    print(f'My Id is {student_id}.')

    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(data_structure, toppings):
    data_structure['pizza_toppings'].extend(toppings)
    data_structure['pizza_toppings'] = sorted([topping.lower() for topping in data_structure["pizza_toppings"]])
    return data_structure

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(data_structure):
    print("My favourite pizza toppings are:")
    for topping in data_structure["pizza_toppings"]:
        print(f"- {topping}")
    print()
    return


# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(data_structure):
    genres = [movie['genre'] for movie in data_structure['movies']]
    print("I like to watch " + ", ".join(genres) + " movies.")

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movies_list):
    titles = [movies['title'].title() for movies in movies_list]
    if len(titles) > 1:
        titles[-1] = 'and ' + titles[-1]
    print("Some of my favourite movies are " + ", ".join(titles) + "!\n")

if __name__ == '__main__':
    main()