#Import librbary and create variable for movie desription to compare to
import spacy

nlp = spacy.load('en_core_web_md')

plant_hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

#Give the user to most similar movie to plant_hulk
def similar_movie(compare_to):
    
    #Create variables to track the most similar movies
    most_similar = ''
    max_sim_rating = 0.0
    compare_nlp = nlp(compare_to)
    
    #Loop through all movies comparing the rating the previous max, saving the highest
    with open('movies.txt', 'r') as file:
        movies = file.readlines()
        
        for movie in movies:
            parse = movie.split(':')
            description = parse[1]
            similiarity = nlp(movie).similarity(compare_nlp)
            
            if similiarity > max_sim_rating:
                most_similar = movie
                max_sim_rating = similiarity
    
    #Display the result
    print(f'''
    ----------------------------------Result------------------------------------------
    The most similar movie with a score of {round(max_sim_rating, 2)} is: 
    
    {most_similar}
    
    -------------------------------------------------------------------------------------------''')

#Call the function to find the most similar movie
similar_movie(plant_hulk)


