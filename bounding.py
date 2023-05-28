import matplotlib.pyplot as plt
from ultralytics import YOLO


def bounding_boxes(img):
    model = YOLO("yolov8n.pt")

    model_output = model(img)[0]

    results = model_output.boxes.boxes.cpu().numpy()

    fig, axs = plt.subplots(1, 1, figsize=(10, 10))
    axs.imshow(img)

    # Plot boxes
    for result in results:
        # Draw square
        axs.add_patch(plt.Rectangle((result[0], result[1]),
                                    result[2] - result[0],
                                    result[3] - result[1],
                                    fill=False,
                                    edgecolor='red',
                                    linewidth=2))

        # Get name
        name = model_output.names[int(result[5])]

        # Draw label
        axs.text(result[0], result[1] - 2,
                 s=str(name) + ' ' + str(round(result[4], 2)),
                 color='white',
                 verticalalignment='top',
                 bbox={'color': 'red', 'pad': 0})

    # Remove axes
    axs.axis('off')

    return fig
