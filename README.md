# PokemonSearch
# Author
Josh Phillips<br>

# About
This program requires the user to enter a CSV filled with Pokemon Cards, loading them into an array of objects.<br>
Then, the user is prompted to input search criteria (requests specific format separated by 6 commas (",,,,,," would be an empty search))<br>
Search Criteria: Type, Minimum Attack Damage, HP, Ablities, Stage, Attack Energy Amount, Attack Energy Type<br>
The program then outputs the results to the user, and prompts the user to either 'exit' or continue searching for Pokemon<br>

# Steps
    1   Start program
    2   Enter CSV file path or just the file name if in the same directory
    3   To continue with searching, hit enter. To exit, type 'exit'
    4   Enter comma separated list of 7 search parameters (again, ",,,,,," indicates no search parameters, "Grass,,,,,," would return all Grass type)
    5   Repeat steps 3 and 4
