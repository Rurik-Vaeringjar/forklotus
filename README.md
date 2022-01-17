# ForkLotus
A fork of pylotus (https://github.com/alex-claman/pylotus). 

This project started out as personal modifications to expand upon and update pylotus to include parts of the warframe api that hadn't been implemented yet. It eventually turned into a project in its own right when additional funtionality and changes went beyond the scope of the original. As such, forklotus occasionally changes the format of incoming api information to make it easier to customize. For example, the 'node' key in the warframe api's fissure information is in the combined format of "node_name (planet_name)". The Fissure response class in forklotus retains this information in a location variable but also splits the information into node and planet variables for easier customization. Forklotus also fixes a host of other problems such as certain keys not always being present in the api and the removal of keys that are no longer present in the warframe api.
