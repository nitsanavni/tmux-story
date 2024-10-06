#!/bin/bash

# Variables
PLUGIN_URL="https://github.com/nitsanavni/typist.nvim"
PLUGIN_NAME="typist"
PLUGIN_DIR="$HOME/.local/share/nvim/site/pack/plugins/start/$PLUGIN_NAME"
INIT_LUA_DIR="$HOME/.config/nvim"
INIT_LUA="$INIT_LUA_DIR/init.lua"
REQUIRE_LINE="require('$PLUGIN_NAME').setup({})"

# Ensure plugin directory exists
mkdir -p "$HOME/.local/share/nvim/site/pack/plugins/start"

# Clone the plugin
if [ ! -d "$PLUGIN_DIR" ]; then
	  echo "Cloning $PLUGIN_NAME into $PLUGIN_DIR..."
	    git clone "$PLUGIN_URL" "$PLUGIN_DIR"
    else
	      echo "$PLUGIN_NAME is already installed."
fi

# Ensure init.lua directory and file exist
mkdir -p "$INIT_LUA_DIR"
touch "$INIT_LUA"

# Check if the require line already exists in init.lua
if grep -q "$REQUIRE_LINE" "$INIT_LUA"; then
	  echo "$PLUGIN_NAME is already configured in init.lua."
  else
	    # Add the require line with setup to init.lua
	      echo "Adding $PLUGIN_NAME configuration to init.lua..."
	        echo "" >> "$INIT_LUA"  # Add a blank line
		  echo "-- Configuration for $PLUGIN_NAME" >> "$INIT_LUA"
		    echo "$REQUIRE_LINE" >> "$INIT_LUA"
		      echo "Added $PLUGIN_NAME to init.lua"
fi

echo "Done!"

