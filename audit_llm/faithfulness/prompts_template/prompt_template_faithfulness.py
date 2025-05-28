CURRENT_VERSION = 4

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
L’entreprise a récemment structuré sa politique RH autour d’un nouveau directeur, chargé de veiller à la stabilité des effectifs. Pour cela, il s’appuie sur une instance renouvelée, à la fois lieu d’écoute et relais du dialogue social au quotidien.
"""  # noqa: E501

example_input_sentence_1 = """
Le CSE (Comité du Soutien Engagé) est présent dans l'entreprise.
"""  # noqa: E501

example_output_1 = """
[
        {{
            "raison": "Faux. La réponse se trompe dans la définition de l'acronyme CSE",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_2 = """
Pour garantir un climat social équilibré, l’entreprise a structuré son dialogue interne autour du CSE et d’un nouveau directeur des Ressources Humaines. Ce tandem veille à l’écoute des collaborateurs, à l’analyse des risques et à la diffusion de valeurs telles que l’honnêteté et l’esprit d’équipe.
"""  # noqa: E501

example_input_sentence_2 = """
L'entreprise a un effectif important et stable.
"""  # noqa: E501

example_output_2 = """
[
        {{
            "raison": "Faux. La réponse mentionne une information non présente dans la source : 'un effectif important et stable'.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_3 = """
Soucieuse d’anticiper les évolutions de son environnement, l’entreprise s’appuie sur des instances structurées pour évaluer les menaces potentielles. Cette démarche s’inscrit dans une gouvernance fondée sur l’intégrité et la vigilance.
"""  # noqa: E501

example_input_sentence_3 = """
L'entreprise a alerté sur le retournement de la conjoncture économique.
"""  # noqa: E501

example_output_3 = """
[
        {{
            "raison": "Faux. La réponse confond le comité des risques de l'entreprise avec l'entreprise dans son ensemble (synecdoque)'.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_4 = """
Pour accompagner son développement et structurer sa culture interne, l’entreprise a mis en place des comités dédiés à la gestion des risques et au dialogue social. Ces dispositifs participent à une gouvernance alignée avec une vision éthique et collective.
"""  # noqa: E501

example_input_sentence_4 = """
Les quatre valeurs de l'entreprise sont : honnêteté, intégrité, impartialité et esprit d’équipe.
"""  # noqa: E501

example_output_4 = """
[
        {{
            "raison": "Vrai. La réponse reprend les valeurs de l'entreprise telles que décrites dans la source.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_5 = """
Avec l’arrivée d’un nouveau directeur des Ressources Humaines, l’entreprise renforce sa stratégie de gestion des effectifs et de dialogue interne. En s’appuyant sur le CSE, instance issue de la réforme des anciennes représentations du personnel, elle favorise un climat d’écoute et de soutien.
"""  # noqa: E501

example_input_sentence_5 = """
La présence du CSE et d'un directeur des Ressources Humaines semble refléter une volonté de l'entreprise de maintenir un dialogue social constructif.
"""  # noqa: E501

example_output_5 = """
[
        {{
            "raison": "Faux. La réponse fait une conjecture qui ne se base par sur les sources (lien entre le CSE et le DRH avec la qualité du dialogue social).",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_6 = """
L’entreprise s’appuie sur une équipe IT solide pour garantir un environnement numérique fiable et sécurisé. Ce service joue un rôle clé dans l’automatisation des processus, la sécurisation des données et l’accompagnement des utilisateurs.
"""  # noqa: E501

example_input_sentence_6 = """
Du matériel informatique spécifique est fourni aux employés.
"""  # noqa: E501

example_output_6 = """
[
        {{
            "raison": "Vrai. La réponse reprend l'idée que du matériel informatique spécifique est fourni aux employés.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_7 = """
L’entreprise conçoit des infrastructures d’analyse performantes, reposant principalement sur des algorithmes d’intelligence artificielle. Ces solutions sont intégrées directement dans les environnements de production de ses clients afin d’optimiser la qualité et l’efficacité.
"""  # noqa: E501

example_input_sentence_7 = """
L'entreprise sait prédire les cas de non conformité de ses produits au cours de l'activité industrielle journalière grâce à l'intelligence artificielle.
"""  # noqa: E501

example_output_7 = """
[
        {{
            "raison": "Faux. La réponse crée un amalgame entre les produits des clients et les produits de l'entreprise.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_8 = """
En combinant expertise technique et intelligence artificielle, l’entreprise développe des solutions d’analyse avancées pour ses clients industriels. Elle mène également des projets novateurs, en interne ou en partenariat, souvent soutenus par le crédit impôt recherche.
"""  # noqa: E501

example_input_sentence_8 = """
L'entreprise investit massivement dans l'innovation.
"""  # noqa: E501

example_output_8 = """
[
        {{
            "raison": "Faux. La réponse mentionne seulement l'innovation sans préciser qu'il s'agit d'un investissement massif. la réponse contient donc une exagération qui n'est pas strictement déductible des sources.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_9 = """
L’entreprise mobilise l’intelligence artificielle pour améliorer la performance industrielle de ses clients, notamment en anticipant les non-conformités. Elle développe des infrastructures d’analyse adaptées, intégrées dans des projets innovants menés en collaboration ou en interne.
"""  # noqa: E501

example_input_sentence_9 = """
Quand c’est possible, l'entreprise automatise ses processus.
"""  # noqa: E501

example_output_9 = """
[
        {{
            "raison": "Vrai. La réponse reprend l'idée de l'automatisation des processus.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_10 = """
Pour garantir un haut niveau de sécurité numérique, l’entreprise s’appuie sur un service informatique structuré et proactif. Ce dernier assure la mise en place d’outils sécurisés, la formation des employés et le respect de règles strictes en matière de cybersécurité.
"""  # noqa: E501

example_input_sentence_10 = """
2 personnes appartenant à l'équipe IT sont dédiées à la sécurité informatique.
"""  # noqa: E501

example_output_10 = """
[
        {{
            "raison": "Vrai. La réponse précise le nombre de personnes dédiées à la sécurité informatique.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_11 = """
Consciente des enjeux liés à la cybersécurité, l’entreprise a structuré son service IT pour protéger ses systèmes et accompagner les utilisateurs. Elle impose des formations et veille à la mise en place de bonnes pratiques informatiques.
"""  # noqa: E501

example_input_sentence_11 = """
L'entreprise a mis en place comme règles de sécurité numérique : une politique de mot de passe rigoureuse et la protection contre les virus.
"""  # noqa: E501

example_output_11 = """
[
        {{
            "raison": "Faux. La réponse produit une information tronquée en oubliant une règle : 'la mise à jour régulière du système informatique'.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_12 = """
Le service informatique de l’entreprise veille à offrir un environnement numérique fiable, adapté aux besoins de chaque service. Dans cette logique, des outils ciblés ont été déployés pour renforcer la confidentialité et l’efficacité des services sensibles.
"""  # noqa: E501

example_input_sentence_12 = """
L'entreprise a pris des mesures spécifiques aux RH avec un réseau wifi et une interface sécurisée.
"""  # noqa: E501

example_output_12 = """
[
        {{
            "raison": "Faux. La réponse produit une information agglomérée en étendant le Wifi seulement aux RH.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_13 = """
L'entreprise a développé une infrastructure informatique solide avec un service IT de 10 personnes, dont 2 spécialisées exclusivement dans la sécurité informatique. Ce service a établi des mesures de protection essentielles incluant une politique de mots de passe rigoureuse, des mises à jour système régulières et une protection antivirale, tout en fournissant du matériel spécialisé et des formations de sécurité aux employés.
"""  # noqa: E501

example_input_sentence_13 = """
La présence d'un service IT et de règles en matière de sécurité informatique pourrait indiquer une volonté de l'entreprise de protéger ses données et celles de ses clients.
"""  # noqa: E501

example_output_13 = """
[
        {{
            "raison": "Faux. La réponse fait une conjecture qui ne se base par sur les sources (lien entre le service IT et les règles de sécurité informatique avec la protection des données).",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_14 = """
L'entreprise dispose d'un service informatique robuste de 10 personnes qui fournit du matériel informatique spécialisé à ses employés pour garantir la qualité de leurs missions. Ce service a également mis en place des formations obligatoires pour sensibiliser le personnel aux règles de sécurité informatique, accompagnant ainsi chaque employé dans l'utilisation appropriée des outils numériques. 
"""  # noqa: E501

example_input_sentence_14 = """
Le service IT aide les employés dans l'apprentissage de l'utilisation du matériel informatique conformément aux règles de sécurité, ce qui semblerait prouver la bienveillance de l'entreprise envers ses employés.
"""  # noqa: E501

example_output_14 = """
[
        {{
            "raison": "Vrai. La réponse confirme la démarche de formation du service IT auprès des employés. Elle fait également une conjecture sur la bienveillance de l'entreprise qui ne se base pas sur les sources.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_15 = """
L'entreprise développe des projets novateurs financés par le crédit impôt recherche, qu'ils soient menés en partenariat avec ses clients ou en interne, tout en automatisant ses processus lorsque cela est possible. Parallèlement, elle a enregistré un gain significatif de 2,7% représentant 1,235 millions d'euros grâce à la mise en place d'un nouveau réseau commercial dans le secteur business incluant les banques Société Générale, BoursoBank et BNP. 
"""  # noqa: E501

example_input_sentence_15 = """
La réalisation de projets innovateurs semble avoir impacté les gains de l'entreprise.
"""  # noqa: E501

example_output_15 = """
[
        {{
            "raison": "Faux. La réponse fait une conjecture qui ne se base par sur les sources (lien entre les projets innovateurs et les gains de l'entrprise).",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_16 = """
L'entreprise se concentre sur le développement de projets novateurs financés par le crédit impôt recherche, réalisés soit en partenariat avec ses clients soit en interne. Elle a également mis en place un nouveau réseau commercial dans le domaine business, incluant des partenariats avec les banques Société Générale, BoursoBank et BNP.
"""  # noqa: E501

example_input_sentence_16 = """
L'entreprise a réalisé un gain de 1.7 millions d'euros.
"""  # noqa: E501

example_output_16 = """
[
        {{
            "raison": "Faux. La réponse mentionne un gain de 1.235 millions d'euros.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_17 = """
L'entreprise développe des projets novateurs financés par le crédit impôt recherche, menés en partenariat avec ses clients ou en interne, tout en automatisant ses processus lorsque cela est possible. Elle a enregistré un gain de 2,7% correspondant à 1,235 millions d'euros grâce à la mise en place d'un partenariat avec les banques Société Générale, BoursoBank et BNP.
"""  # noqa: E501

example_input_sentence_17 = """
Le nouveau réseau commercial de l'entreprise concerne le domaine de la finance.
"""  # noqa: E501

example_output_17 = """
[
        {{
            "raison": "Vrai. La réponse s'appuie sur l'information du nouveau réseau commercial et de sa composition.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_18 = """
L'entreprise automatise ses processus et développe des projets innovants en partenariat avec ses clients ou en interne, souvent soutenus par le crédit impôt recherche. Elle met également en place des infrastructures d’analyse basées sur l’intelligence artificielle pour anticiper les non-conformités en production.
"""  # noqa: E501

example_input_sentence_18 = """
Sur le plan entreprise un gain de 2.7% a été réalisé.
"""  # noqa: E501

example_output_18 = """
[
        {{
            "raison": "Faux. La réponse traduit le mot 'business' en 'entreprise' qui peut nuire au sens global de la phrase. ",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_19 = """
L'entreprise accompagne ses clients en installant des infrastructures d’analyse reposant sur des algorithmes d’intelligence artificielle, capables de détecter les non-conformités en amont. Elle valorise également l'innovation à travers des projets soutenus par le crédit impôt recherche.
"""  # noqa: E501

example_input_sentence_19 = """
Sur le plan business, l'entreprise a réalisé un gain de 2.7%.
"""  # noqa: E501

example_output_19 = """
[
        {{
            "raison": "Vrai. La réponse reprend l'idée du gain de 2.7% sur le plan business.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_20 = """
L’entreprise renforce son engagement social en s’appuyant sur le CSE pour assurer un dialogue constructif avec les salariés et sur le comité des risques pour anticiper les évolutions économiques. Elle veille également au bien-être de ses collaborateurs, comme en témoignent la baisse des arrêts maladie et l’acceptation de congés sabbatiques.
"""  # noqa: E501

example_input_sentence_20 = """
En 2025, le nombre de nouveaux collaborateurs est de 30.
"""  # noqa: E501

example_output_20 = """
[
        {{
            "raison": "Faux. La réponse confond les années. Le nombre de 30 nouveaux collaborateurs correspond à l'année 2023 comme mentionné dans le titre du document '2023_04_12' et non 2025",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_21 = """
L’entreprise a renforcé sa politique sociale avec l’arrivée d’un nouveau directeur des Ressources Humaines, appuyé par le CSE pour garantir un climat de travail serein. Elle a également favorisé le bien-être des salariés, tout en poursuivant sa croissance.
"""  # noqa: E501

example_input_sentence_21 = """
En 2023, l'effectif total est de 2025 personnes.
"""  # noqa: E501

example_output_21 = """
[
        {{
            "raison": "Vrai. La réponse menttionne correctement l'éffectif total pour l'année désignée.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_previous_sentences_22 = """
L’entreprise place le bien-être de ses salariés au cœur de ses priorités, comme en témoigne la baisse des arrêts maladie et l’instauration d’un dialogue social actif via le CSE.
"""  # noqa: E501

example_input_sentence_22 = """
Les collaborateurs demandent des congés sabbatiques.
"""  # noqa: E501

example_output_22 = """
[
        {{
            "raison": "Faux. Il y a une généralisation entre deux collaborateurs et l'ensemble des salariés",
            "label": "0",
        }}
]
"""  # noqa: E501

example_previous_sentences_ = """

"""  # noqa: E501

example_input_sentence_ = """

"""  # noqa: E501

example_output_ = """
[
        {{
            "raison": "",
            "label": "",
        }}
]
"""  # noqa: E501


prompt_template = f"""
            ### **Rôle du LLM Juge** : 
            Votre mission est d'analyser la véracité des phrases fournies par rapport à des documents de référence. Dès qu'une information de la phrase est non-déductible des sources, alors toute la phrase doit être classée comme non-déductible.

            Les données qui vous seront fournies sont :
            - Sources : Les documents de référence.
            - Paragraphe : Le paragraphe contextualisant la phrase.
            - Phrase : la phrase dont vous devez évaluer le caractère déductible.

            ### **Instructions d'évaluation** :
            Adoptez l'approche suivante dans votre évaluation :
            - Lire les sources en entier.
            - Lire le paragraphe en entier.
            - Lire la phrase en entier.
            - Pour chaque phrase verbalisez un raisonnement pas à pas sur le caractère déductible des informations de la phrase par rapport aux sources.
            - Si les informations de la phrases sont insuffisants ou ambigües, vous pouvez utiliser vos connaissances du monde pour déterminer si toutes ces informations sont réellement déductibles des sources.
            - En déduire une évaluation finale pour la phrase.
            - Chaque évaluation est un label. 
                - Soit 0 : au moins une information n'est pas déductible des sources. 
                - Soit 1 : toutes les informations sont déductibles des sources.

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

            **Exemple 6**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_6}
            Exemple de phrase :
            {example_input_sentence_6}
            Exemple de réponse au format JSON :
            {example_output_6}

            **Exemple 7**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_7}
            Exemple de phrase :
            {example_input_sentence_7}
            Exemple de réponse au format JSON :
            {example_output_7}

            **Exemple 8**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_8}
            Exemple de phrase :
            {example_input_sentence_8}
            Exemple de réponse au format JSON :
            {example_output_8}

            **Exemple 9**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_9}
            Exemple de phrase :
            {example_input_sentence_9}
            Exemple de réponse au format JSON :
            {example_output_9}

            **Exemple 10**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_10}
            Exemple de phrase :
            {example_input_sentence_10}
            Exemple de réponse au format JSON :
            {example_output_10}

            **Exemple 11**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_11}
            Exemple de phrase :
            {example_input_sentence_11}
            Exemple de réponse au format JSON :
            {example_output_11}

            **Exemple 12**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_12}
            Exemple de phrase :
            {example_input_sentence_12}
            Exemple de réponse au format JSON :
            {example_output_12}

            **Exemple 13**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_13}
            Exemple de phrase :
            {example_input_sentence_13}
            Exemple de réponse au format JSON :
            {example_output_13}

            **Exemple 14**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_14}
            Exemple de phrase :
            {example_input_sentence_14}
            Exemple de réponse au format JSON :
            {example_output_14}

            **Exemple 15**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_15}
            Exemple de phrase :
            {example_input_sentence_15}
            Exemple de réponse au format JSON :
            {example_output_15}

            **Exemple 16**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_16}
            Exemple de phrase :
            {example_input_sentence_16}
            Exemple de réponse au format JSON :
            {example_output_16}

            **Exemple 17**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_17}
            Exemple de phrase :
            {example_input_sentence_17}
            Exemple de réponse au format JSON :
            {example_output_17}

            **Exemple 18**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_18}
            Exemple de phrase :
            {example_input_sentence_18}
            Exemple de réponse au format JSON :
            {example_output_18}

            **Exemple 19**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_19}
            Exemple de phrase :
            {example_input_sentence_19}
            Exemple de réponse au format JSON :
            {example_output_19}

            **Exemple 20**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_20}
            Exemple de phrase :
            {example_input_sentence_20}
            Exemple de réponse au format JSON :
            {example_output_20}

            **Exemple 21**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_21}
            Exemple de phrase :
            {example_input_sentence_21}
            Exemple de réponse au format JSON :
            {example_output_21}

            **Exemple 22**
            Exemple de sources :
            {example_source}
            Exemple de paragraphes :
            {example_previous_sentences_22}
            Exemple de phrase :
            {example_input_sentence_22}
            Exemple de réponse au format JSON :
            {example_output_22}


            Voici les données :
            Sources :
            {{sources}}
            Paragraphe :
            {{previous_sentences}}
            Phrase :
            {{phrase}}
            JSON:
            """  # noqa: E501
