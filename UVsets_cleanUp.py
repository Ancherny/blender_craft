// This is a Blender sript to clean up all the UV maps/sets
// from selected polygonal objects, except the currently
// active for render, and set it a new name.
//
// created by: MAxim Moshkov | Pixonic |My.Games
// date created: April 06, 2023
//
// updated by: Andrew Chernyshov aka Ancher | My.Games
// date updated: April 06, 2023
//
// original idea & request: Alexey Borzykh aka NURB | My.Games
//
// How to use:
// Open Tex Editor window and load the script.
// Go to the line at the bottom: new_uv_map_name = "UVMap0".
// Change UVMap0 name to the one you prefer.
// Select all polygonal objects you want to clean up.
// Hit the [run] button.
// Check the result.
// Go get yourself a coffe as you just saved precious time
// instead of paintstakingly process each mesh manually.
// Prise those smart people listed above.


import bpy

def remove_uv_maps_except_active(obj):
    render_uv_layer = next((uv_layer for uv_layer in obj.data.uv_layers if uv_layer.active_render), None)
    if render_uv_layer is None:
        return

    uv_maps_to_remove = [uv_map for uv_map in obj.data.uv_layers if uv_map != render_uv_layer]
    for uv_map in reversed(uv_maps_to_remove):
        if uv_map.name in obj.data.uv_layers:
            obj.data.uv_layers.remove(uv_map)

def rename_active_uv_map(obj, new_name):
    render_uv_layer = next((uv_layer for uv_layer in obj.data.uv_layers if uv_layer.active_render), None)
    if render_uv_layer is not None:
        old_name = render_uv_layer.name
        render_uv_layer.name = new_name
        print(f"Renamed UV layer from '{old_name}' to '{new_name}'")

def process_objects(new_uv_map_name):
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            remove_uv_maps_except_active(obj)
            rename_active_uv_map(obj, new_uv_map_name)

new_uv_map_name = "UVMap0"
process_objects(new_uv_map_name)
