from utils.dataset import Yoga_82
import torch


def create_dataset(path, file_name, transformations =  False, prueba = True, nivel = 6, n_samples = 1000):
    """Método que genera los objetos de tipo Dataset Yoga-82

    Args:
        path (str): ruta del proyecto
        file_name (str): ruta del archivo que contiene la información de las imágenes
        transformations (bool, opcional): Si se le debe realizar transformaciones al dataset.
        prueba (bool, opcional): indica si es un dataset de prueba o no.
        nivel (int, opcional): indica la jerarquía de clases.
        n_samples (int, opcional): indica la cantidad de muestras a usar en el caso que sea de prueba.

    Returns:
        _type_: _description_
    """

    dataset = Yoga_82(root = path, 
                            file_ = file_name, 
                            transform = transformations, 
                            prueba = prueba, 
                            nivel = nivel,
                            n_samples = n_samples)
    return dataset


def create_dataloaders(dataset, set_ = 'train', batch_size = 32, val_size = 0.2):
    """Método que genera los dataloader para usarlos en entrenamiento.

    Args:
        dataset (torch.Dataset): dataset a instaciar como data loaders
        set_ (_type_): conjunto de datos.
        batch_size (int, optional): tamaño del batch.
        val_size (float, optional): proporción de datos a usar como validación. 

    Returns:
        DataLoaders: retorna los objetos de tipo dataloaders.
    """

    if set_ == 'train':

        train_size = int((1 - val_size) * len(dataset))
        test_size = len(dataset) - train_size
        train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size, shuffle=True)

        return train_loader, val_loader
    else:
        test_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
        return test_loader