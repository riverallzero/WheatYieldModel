from PIL import Image
import os
import cv2


def main():
    output_dir = "../Output/figures"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images_list = [["../output/figures/freshweight.png", "../output/figures/lai.png"],
                   ["../output/figures/length.png", "../output/figures/spad.png"],
                   ["../output/figures/watercontent.png", "../output/figures/width.png"]]

    width = 3000
    height = 600

    for i in range(len(images_list)):
        images = [Image.open(x) for x in images_list[i]]
        new_im = Image.new('RGB', (width, height))
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        new_im.save(os.path.join(output_dir, f"image_{i}.png"))

    images_list = [cv2.imread("../output/figures/image_0.png"),
                   cv2.imread("../output/figures/image_1.png"),
                   cv2.imread("../output/figures/image_2.png")]

    im_v = cv2.vconcat(images_list)
    cv2.imwrite(os.path.join(output_dir, f"data_plot.png"), im_v)


if __name__ == "__main__":
    main()