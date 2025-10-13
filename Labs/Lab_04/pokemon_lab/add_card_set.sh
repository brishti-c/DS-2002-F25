#!/bin/bash

# Prompt the user for the TCG Card Set ID
read -p "Enter the TCG Card Set ID (e.g., base1, base4): " SET_ID

# Check if the input is empty
if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

# Let the user know we're fetching the data
echo "Fetching card data for set ID: $SET_ID ..."

# Fetch data using curl and save it as a JSON file named after the set ID
curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "card_set_lookup/${SET_ID}.json"

# Confirm completion
echo "Card data for set '$SET_ID' has been saved to card_set_lookup/${SET_ID}.json"
