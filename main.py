import shutil
from copy_static import copy_src_to_dst
from markdown_to_blocks import markdown_to_html_node
from generate_page import extract_title, generate_page

src = "./static"
dst = "./public"
generate_page_src = "./content/index.md"
template_path = "./template.html"
generate_page_dst = "./public/index.html"

if __name__ == "__main__":
    print(f"deleting {dst} directory...")
    if os.path.exists(os.path.abspath(dst)):
        shutil.rmtree(os.path.abspath(dst))
    os.mkdir(dst)
    print(f"copying {src} --> {dst}")
    copy_src_to_dst(src, dst)

    generate_page(generate_page_src, template_path, generate_page_dst)

