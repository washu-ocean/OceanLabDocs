Sylvester drive storage structure
=================================

The "Sylvester drive" is the shared storage space used by the SEAL lab to conduct preprocesing of anatomical/functional MRI data and subsequent analyses. Below is a list of the Sylvester drive's top-level directories, stored at ``/data/sylvester/data1/`` if accessed over SSH/VNC Viewer::

    /data/sylvester/data1/
    ├── analysis/
    ├── analysis_revision_in_progress/
    ├── archive/
    ├── CIFTI_RELATED/
    ├── config/
    ├── datasets/
    ├── dvc-raw/
    ├── dvc-remotes/
    ├── LabOrientation/
    ├── meta/
    ├── packages/
    ├── perino/
    ├── projects/
    ├── ref/
    ├── scripts/
    ├── scripts_archive/
    ├── shark/
    ├── software/
    ├── test/
    ├── users/
    └── wdfs-master/

.. attention::

   This list of directories is always subject to change, and not all of these listed above are used on a regular basis anymore. The directories we'll be explaining more in-depth on this page should be those that are almost guaranteed to stay around in the long-long-term.

We'll discuss the few directories you'll likely be interacting with regularly in this guide.

``datasets/``
-------------

The ``datasets/`` directory contains all of the raw and preprocessed functional/anatomical MRI data for our studies, and sometimes some derivative outputs depending on the type of study. Each subfolder within this directory represents a different study or analysis project being conducted by the lab, which each have their own internal structure decided by those working with the data.

If you are needing to store data that you know will be accessed by multiple people, don't hesitate to create a directory under ``datasets/``, name it something descriptive, and optionally create a "README.txt" file to explain to users how your directory is structured. 

Going forward, the lab is moving toward using the `BIDS <https://bids-specification.readthedocs.io/>`_ specification, which allows us to perform preprocessing and analyses in an easily reproducible, transparent manner. For more information on how to create a new dataset using the BIDS spec, see :doc:`/new_datasets`. 




