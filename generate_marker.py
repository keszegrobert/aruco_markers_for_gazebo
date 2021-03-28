import argparse
from datetime import datetime
from jinja2 import Template

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage = 'generate collada files for a marker id from a specific dictionary'
    )

    parser.add_argument('-t', '--template',
        default = 'template.dae',
        help = 'bits of the marker it can be [4,5,6,7]'
    )

    parser.add_argument('-p', '--png',
        default = 'marker.png',
        help = 'bits of the marker it can be [4,5,6,7]'
    )

    parser.add_argument('-n', '--name',
        default = 'marker',
        help = 'name of the marker'
    )
    
    parser.add_argument('-i', '--id',
        default = 0,
        help = 'id if the marker'
    )

    parser.add_argument('-o', '--output',
        default = 'output.dae'
    )

    args = parser.parse_args()

    template = ''
    with open('template.dae') as f:
        template = f.read()
    j2_template = Template(template)

    data = {
        "png_file": args.png,
        "png_name": args.name,
        "authoring_tool": "generate_marker.py",
        "author": "Marker Generator",
        "creation_date": datetime.now().strftime("%Y-%m-%dT%H:%M:%s"),
        "modification_date": datetime.now().strftime("%Y-%m-%dT%H:%M:%s"),
        "scale": 0.025
    }

    with open(args.output, "w") as f:
        f.write(j2_template.render(data))
    