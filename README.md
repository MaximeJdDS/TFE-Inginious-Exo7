# Cours Informatique avec Inginious

Ce projet vise à fournir un cours d'informatique en utilisant la plateforme Inginious pour enseigner le langage de programmation Python aux étudiants du secondaire en français.

## Fonctionnalités

1. **Correction Automatique :** Le système corrige automatiquement le code soumis par les étudiants, en fournissant un feedback adapté.

2. **Tagging des Soumissions :** Les soumissions des étudiants sont "taggées" pour permettre aux professeurs de repérer facilement les différentes difficultés rencontrées par l'auditoire, sans avoir à relire chaque copie manuellement.

3. **Continuous Integration :** Intégration continue pour assurer la stabilité et la fiabilité du système.

## Dépendances

Ce projet dépend du projet Inginious disponible à [ce lien](https://github.com/UCL-INGI/INGInious). Veuillez vous référer à sa documentation pour les détails d'installation et de configuration.

## Instructions d'Installation

Le système est déjà en ligne, donc aucune instruction d'installation n'est nécessaire. Vous pouvez accéder à la plateforme [ici](https://inginious.org/course/exo7).

## Structure du Répertoire

- **ResultTFE** : répertorie toutes les données relatives aux résultats de validation pour le TFE.
- **.github/workflows** + **inginious/frontend** : pour l'intégration continue.
- **course.yaml** + **taskset.yaml** : représente la structure du cours.
- **$common** : répertoire regroupant toutes les ressources disponible pour tous les exercices.
Le reste sont des exercices ayant comme structure :
  - **/src** : contient le fichier de test ainsi que le fichier de l'étudiant.
  - **/test** : contient la ou les soumissions à retester pour l'intégration continue.
  - **run** : le fichier permettant d'éxcécuter l'exercice.
  - **task.yaml** : contient toute la strucuture de l'exercice.
 
Tous les autres dossiers représentent des exercices.

