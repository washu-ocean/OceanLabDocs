Storage structure
=================

The storage owned by the lab can be split into two categories: the Sylvester drive and scratch drives.

Sylvester drive
===============

The "Sylvester drive" is the shared storage space used by the SEAL lab to conduct preprocesing of anatomical/functional MRI data and subsequent analyses. Some things to note:

1. "Snapshots" of the entire drive are taken every weekday, with a maximum of 30 snapshots stored at any given time. A snapshot is essentially a copy of the entire filesystem at some point in time that can be explored; if an important file on this drive is deleted, or you'd simply like to revert a file/directory to a previous version, see :ref:`_restoring-files-using-snapshots`.
2. Since snapshots are stored on the same drive and actively take up space, *it is important to not add any unnecessarily-large files to the drive*, as they will be included in subsequent snapshots. If a large file is present in some (or all) of the snapshots currently in storage, the file cannot truly be deleted until the snapshots it appears on are deleted after enough time passes.

Here are some examples of things that are typically stored on the Sylvester drive:

- Fully-preprocessed functional/anatomical MRI data
- Raw MRI session data before preprocessing in NIFTI format 
- Installed software (i.e. MATLAB, R, Python, Conda environments, etc.)
- Finalized analyses
- Analyses currently in progress, depending on how much space they take up.  

Here are some examples of things to avoid leaving on the Sylvester drive, if possible:

- Intermediate files created as a result of data preprocessing
- Output of exploratory analyses that aren't considered to be in a finalized state
- Raw DICOM data after it has been converted into NIFTI format

If you need to store file that fall more into this category, see :ref:`_scratch-drives`.

Sylvester drive structure
-------------------------

Below is a list of the Sylvester drive's top-level directories, stored at ``/data/sylvester/data1/`` if accessed over SSH/VNC Viewer::

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
^^^^^^^^^^^^^

The ``datasets/`` directory contains all of the raw and preprocessed functional/anatomical MRI data for our studies, and sometimes some derivative outputs depending on the type of study. Each subfolder within this directory represents a different study or analysis project being conducted by the lab, which each have their own internal structure decided by those working with the data.

If you are needing to store data that you know will be accessed by multiple people, don't hesitate to create a directory under ``datasets/``, name it something descriptive, and optionally create a "README.txt" file to explain to users how your directory is structured. 

Going forward, the lab is moving toward using the `BIDS <https://bids-specification.readthedocs.io/>`_ specification, which allows us to perform preprocessing and analyses in an easily reproducible, transparent manner. For more information on how to create a new dataset using the BIDS spec, see :doc:`/new_datasets`. 

``LabOrientation/``
^^^^^^^^^^^^^^^^^^^

This directory should contain a couple different important files/directories:

- The source files for these docs
- A file named ``template_bashrc``, which chooses some nice settings for using Bash over SSH on Wallace. See :ref:`configuring-bash` for more info.

``ref/``
^^^^^^^^

This directory contains files commonly used across different analysis projects. These include:

- Volumetric/surface atlases generated from different population samples, which vary by population (i.e. adult-space vs. neonatal-space), coordinate system (i.e. Talaraich vs. MNI space), and resolution.
- Various parcellation-related files
- Finalized outputs from already-published studies

``scripts/ and software/``
^^^^^^^^^^^^^^^^^^^^^^^^^^

These directories contain installations of software not installed at the root level; this allows the lab's programmers to configure/change them as needed. You shouldn't typically need to directly interact with these directories.

``users/``
^^^^^^^^^^

Each folder under this directory is owned by a specific user on the system, and is meant to act as a personal home directory for each user. 

The difference between these directories and your default home directories at ``~`` is that there is no upper bound on storage here, where there is at ``~``. People using Wallace typically only keep files in ``~`` that are used for configuration, such as the ``.bashrc``.


.. _restoring-files-using-snapshots:

Restoring files using ZFS snapshots
-----------------------------------

.. _scratch-drives:

Scratch drives
==============

