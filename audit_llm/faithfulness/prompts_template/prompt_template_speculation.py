CURRENT_VERSION = 1

json_schema = """
```json
{{
    "raison": "Le raisonnement justifiant le label.",
    "label": "1"
}}
"""

example_source = """
-Rapport_entreprise_2023_04_12-
Analyse génrale de l'entreprise.
L'entreprise s'est dôté d'un nouveau directeur des Ressources Humaines. Ce dernier pilote notamment la stabilité des effectifs. Pour cela, il s'appuie sur le CSE. Ce dernier permet d'offrir une espace d'écoute, de dialogue et de soutien qui peut faire toute la différence dans le quotidien professionnel.
Le CSE (Comité Social et Économique) s'est substitué aux anciennes instances représentatives du personnel (IRP) : délégués du personnel, comité d'entreprise et CHSCT.
Le CSE, une des principales sources de relations collectives au travail, est la nouvelle instance représentative du personnel mise en place par l’ ordonnance n° 2017-1386 du 22 septembre 2017 relative à la nouvelle organisation du dialogue social et économique dans l'entreprise .
L'entreprise dispose d'un autre comité : 'le comité des risques'. Ce dernier analyse les risques liés à l'activité de l'entreprise. Il a d'ailleurs alerté en novembre 2022 sur le retournement de la conjoncture économique.
Pour donner corps à sa vision, l'entreprise a décidé d'incarner quatre valeurs : honnêteté, intégrité, impartialité et esprit d’équipe.
L'entreprise est également soucieuse du bien être de ses collaborateurs. Elle a par exemple accepté un congés sabbatiques d'une durée d'un an pour deux de ses employés. En parallèle, les arrêts maladies ont diminué de 5% par rapport à l'année précédente.
Cette année le nombre de recrutement a augmenté. Il s'établit à 30 collaborateurs en plus ce qui porte les effectifs à 2025 personnes.


En ce qui concerne la dimension technique de l'entreprise, ses missions sont :
    - Mettre en place chez ses clients des infrastructures d'analyse. Ces infrastructures sont majoritairement composées d'algorithmes d'IA. 
    - Savoir prédire les cas de non conformité des produits au cours de l'activité industrielle journalière de ses clients grâce à l'intelligence artificielle.
    - Réaliser des projets novateurs en recourant à l'innovation. Ces projets sont réalisés en partenariat avec ses clients ou en interne. Ils sont financés par le crédit impôt recherche.
L'entreprise automatise ses processus quand c’est possible.

L'entreprise s'est doté d'un service informatique robuste. Ce service IT est composé de 10 personnes. Afin de maintenir l'entreprise à un haut niveau d'exigence, le service IT a :
    - mis en place un réseau wifi et une interface sécurisée pour les RH. 
    - fourni du matériel informatique spécifique aux employés pour assurer la qualité de leur mission.
    - impose une formation aux employés relatif aux règles de sécurité en ce qui concerne l'utilisation du matériel informatique.
Un sous-service, comprenant 2 personnes, est dédié à la sécurité informatique. En effet, à l’ère du numérique, les menaces informatiques évoluent sans cesse, mettant à l’épreuve la résilience des systèmes d’information.
Ainsi, il a édicté 3 règles de sécurité numérique de base. Ces dernières sont : une politique de mot de passe rigoureuse, la mise à jour régulière du système informatique et la protection contre les virus.
    

Enfin, sur le plan business, l'entreprise a réalisé un gain de 2.7% correspondant à 1.235 millions d'euros. Ce gain est le résultat de la mise en place d'un nouveau réseau commercial. 
Celui-ci concerne le domaine de la finance. Il est composé des banques Société Générale, BoursoBank et BNP.
"""  # noqa: E501

example_previous_sentences_1 = """
L’entreprise a récemment structuré sa politique RH autour d’un nouveau directeur, chargé de veiller à la stabilité des effectifs. Pour cela, il s’appuie sur une instance renouvelée, à la fois lieu d’écoute et relais du dialogue social au quotidien."""  # noqa: E501

example_input_sentence_1 = """
Le CSE (Comité du Soutien Engagé) est présent dans l'entreprise.
"""  # noqa: E501

example_output_1 = """
[
        {{
            "raison": "Faux. La réponse est non spéculative, l'ensemble des faits sont objectifs.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_2 = """
Avec l’arrivée d’un nouveau directeur des Ressources Humaines, l’entreprise renforce sa stratégie de gestion des effectifs et de dialogue interne. En s’appuyant sur le CSE, instance issue de la réforme des anciennes représentations du personnel, elle favorise un climat d’écoute et de soutien."""  # noqa: E501

example_input_sentence_2 = """
La présence du CSE et d'un directeur des Ressources Humaines semble refléter une volonté de l'entreprise de maintenir un dialogue social constructif.
"""  # noqa: E501

example_output_2 = """
[
        {{
            "raison": "Vraie. La réponse est spéculative. Une hypothèse est formulée au travers de 'semble refléter'.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_3 = """
À l’ère du numérique, les menaces informatiques évoluent sans cesse, mettant à l’épreuve la résilience des systèmes d’information. Pour y faire face, l'entreprise a investi dans des compétences et des moyens adaptés.
"""  # noqa: E501

example_input_sentence_3 = """
2 personnes appartenant à l'équipe IT sont dédiées à la sécurité informatique.
"""  # noqa: E501

example_output_3 = """
[
        {{
            "raison": "Faux. La réponse est non spéculative, l'ensemble des faits sont objectifs.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_4 = """
En combinant l’intelligence artificielle à des infrastructures d’analyse sur mesure, l’entreprise aide ses clients à anticiper les non-conformités et à optimiser leur production. Cette capacité à transformer la donnée en levier de performance se traduit également par des projets innovants, menés en interne ou en partenariat, et soutenus par le crédit impôt recherche.
"""  # noqa: E501

example_input_sentence_4 = """
La réalisation de projets innovateurs semblerait avoir impacté les gains de l'entreprise.
"""  # noqa: E501

example_output_4 = """
[
        {{
            "raison": "Vraie. La réponse est spéculative. Une hypothèse est formulée au travers du conditionnel 'semblerait'.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_5 = """
L’entreprise s’appuie sur un service informatique structuré, composé de dix personnes, dont une équipe dédiée à la sécurité numérique. Ce service veille à la qualité des équipements, à la formation des employés, ainsi qu’à la mise en place de règles strictes en matière de cybersécurité.
"""  # noqa: E501

example_input_sentence_5 = """
La présence d'un service IT et de règles en matière de sécurité informatique pourrait indiquer une volonté de l'entreprise de protéger ses données et celles de ses clients.
"""  # noqa: E501

example_output_5 = """
[
        {{
            "raison": "Vraie. La réponse est spéculative. Une supposition est formulée au travers du conditionnel 'pourrait'.",
            "label": "1",
        }}
]
"""  # noqa: E501

prompt_template = f"""
            ### **Rôle du LLM Juge** : 
            Votre mission est d'analyser si les phrases fournies contiennent une forme de spéculation. Une phrase est considérée comme spéculative si elle contient :
            - un jugement ou une opinion,
            - une hypothèse ou une intention supposée,
            - une possibilité formulée au conditionnel ou via des verbes modalisateurs (sembler, pouvoir, envisager, indiquer que, suggérer que, etc.).
            - une conjecture ou une supposition.
            - une intention ou une cause supposée.
            - une évaluation subjective ou un jugement de valeur.
            À l'inverse, une phrase est considérée comme non spéculative si elle énonce un fait observable, mesurable ou vérifiable, sans faire appel à une intention, une cause supposée, une généralisation, ou un raisonnement plausible non étayé.

            Les données qui vous seront fournies sont :
            - Sources : Des extraits de documents de référence.
            - Paragraphe : Un extrait du paragraphe contextualisant la phrase.
            - Phrase : la phrase dont vous devez évaluer le caractère spéculatif.

            ### **Instructions d'évaluation** :
            Adoptez l'approche suivante dans votre évaluation :
            - Lire les sources en entier.
            - Lire le paragraphe en entier.
            - Lire la phrase en entier.
            - Pour chaque phrase verbalisez un raisonnement pas à pas sur le caractère spéculatif ou non spéculatif des informations de la phrase par rapport aux sources en vous basant sur les tournures linguistiques utilisées.
            - En déduire une évaluation finale pour la phrase.
            - Chaque évaluation est un label. 
                - Soit 0 : la phrase est non-spéculative, l'ensemble des faits sont objectifs. 
                - Soit 1 : au moins une information de subjectivité ou de spéculation est présente. Même si les faits sont confirmés par la source, la phrase est jugée spéculative si la formulation laisse place à l’interprétation ou à l’incertitude

            ### **Format des réponses** :
            Vous devez renvoyer uniquement un JSON dans la structure suivante :
            {json_schema}

            Important : Le contenu renvoyé doit être un JSON strictement valide, sans texte supplémentaire, sans explication ni commentaire, directement parsable et la clé « verdicts » devant correspondre à une liste d'objets JSON.

            ### **Exemples** :
            Voici un ensemble d'exemples de phrases et de leurs évaluations.

            **Exemple 1**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_1}
            Exemple de phrase :
            {example_input_sentence_1}
            Exemple de réponse au format JSON :
            {example_output_1}

            **Exemple 2**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_2}
            Exemple de phrase :
            {example_input_sentence_2}
            Exemple de réponse au format JSON :
            {example_output_2}

            **Exemple 3**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_3}
            Exemple de phrase :
            {example_input_sentence_3}
            Exemple de réponse au format JSON :
            {example_output_3}

            **Exemple 4**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_4}
            Exemple de phrase :
            {example_input_sentence_4}
            Exemple de réponse au format JSON :
            {example_output_4}

            **Exemple 5**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_5}
            Exemple de phrase :
            {example_input_sentence_5}
            Exemple de réponse au format JSON :
            {example_output_5}


            Voici les données :
            Sources :
            {{sources}}
            Paragraphe :
            {{previous_sentences}}
            Phrase :
            {{phrase}}
            JSON:
            """  # noqa: E501
