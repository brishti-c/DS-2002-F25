#!/bin/bash

# Let the user know we're starting the refresh
echo "Refreshing all card sets in card_set_lookup/ ..."

# Loop through each JSON file in the lookup directory
for FILE in card_set_lookup/*.json; do

    # Extract the set ID from the filename
    SET_ID=$(basename "$FILE" .json)

    # Notify which set is being updated
    echo "Updating card set: $SET_ID ..."

    # Fetch updated data from the Pokémon TCG API
    curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "$FILE"

    # Confirm the data was written
    echo "Updated data saved to $FILE."
done

# Notify completion
echo "All card sets have been refreshed successfully."
