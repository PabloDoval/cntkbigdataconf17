import cntk as C


def init_reader(path, input_dim, num_label_classes, is_training=True):

    labelStream = C.io.StreamDef(
        field='labels', shape=num_label_classes, is_sparse=False)
    featureStream = C.io.StreamDef(
        field='features', shape=input_dim, is_sparse=False)
    deserializer = C.io.CTFDeserializer(path, C.io.StreamDefs(
        labels=labelStream, features=featureStream))
    return C.io.MinibatchSource(deserializer, randomize=is_training, max_sweeps=C.io.INFINITELY_REPEAT if is_training else 1)
