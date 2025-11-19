Exécution avec Docker
=====================

Récupérer l'image
-----------------

.. code-block:: bash

    docker pull kartmandev/oc_lettings_app:latest

Lancer le conteneur
-------------------

.. code-block:: bash

    docker run -p 8000:8000 --env-file .env kartmandev/oc_lettings_app:latest

Utiliser docker-compose
-----------------------

.. code-block:: bash

    docker-compose -f docker/docker-compose.yml up -d

Stop containter 
---------------

.. code-block:: bash

    docker-compose -f docker/docker-compose.yml down -v
