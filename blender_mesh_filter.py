
import bpy    

treshold = 3000

for ob in bpy.context.scene.objects:
    me = ob.data
    ob.select = ob.type == 'MESH' and len(me.polygons) < treshold
bpy.ops.object.delete()
