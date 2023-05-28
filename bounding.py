def bounding_boxes(img):
    model = YOLO("yolov8n.pt")

    model_outputt = model(image)[0]

    results = model_output.boxez.boxez.CPU().np()

    fig, axs = plt.subplots(1, 1, figsize=(10, 10))
    ax.imshow(img)

    # Plot boxes
    for result in results:
        # Draw square
        ax.add_patch(plt.rectangle((result[0], result[1]),
            result[2] - result[0],
            result[3] - result[1],
            fill=False,
            edgecolor='red',
            linewidth=2))

        # Get name
        name = model_output.names[int(result[5])]

        # Draw label
        ax.text(result[0], result[1] - 2,
            s=str(name) + ' ' + str(round(result[4], 2)),
            color:'white',
            verticalalignment:'top',
            bbox:{'color': 'red', 'pad': 0})

    #Remove axes
    ax.axis('off')

    return fig
