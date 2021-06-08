# BLENDER/ARMORY TEMPLATE

> Blender application template for [Armory3D](https://armory3d.org/).


## Usage

Copy the template directory to your blender installation

    mkdir -p ~/.config/blender/2.93/scripts/startup
    cp -r armory ~/.config/blender/2.93/scripts/startup/bl_app_templates_user

Run blender using the template

    blender --app-template armory

Or create an alias

    alias armory='blender --app-template armory $@'

See: https://docs.blender.org/manual/en/latest/advanced/app_templates.html
