# Blender utilities
Collection of small scripts and functions that don't deserve their own repository.

## Origin To Selected
`bl_idname`: `mesh.origin_to_selected`

Move origin of the mesh to selection.

## Separate Clone
`bl_idname`: `mesh.separate_clone`

Separate selection without deleting.

## Seams From Sharp Edges.
`bl_idname`: `mesh.seams_from_sharp`

Create seams from current sharp edges.

## Toggle SubD modifier.
`bl_idname`: `mesh.toggle_subd`

Toggle show_viewport option in current first Subsurf modifier or create one if there's none.

## Toggle SubD Cage.
`bl_idname`: `mesh.toggle_subd_cage`

Toggle show_on_cage option in current first Subsurf modifier.

## Reload Images.
`bl_idname`: `system.reload_images`

Reload all loaded images.

# Installation
* Click on `Install from File` button in User Preferences Add-on tab and point it to the python file of the add-on you want to add.
* Add shortcut for `bl_idname` of that add-on.
