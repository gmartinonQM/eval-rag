CURRENT_VERSION = 3


json_schema = """
```json
{{
    "raison": "Le raisonnement justifiant le label.",
    "label": "1"
}}
"""

example_question = """
Lors de l'évaluation des changements prévus dans les programmes de rémunération et d'avantages sociaux de l'agence immobilière, comment ces ajustements sont-ils alignés sur la stratégie globale de l'entreprise et quels sont les mécanismes d'analyse mis en place pour mesurer l'efficacité de ces changements, tant sur le plan comptable qu'en termes de satisfaction des employés ?
"""  # noqa: E501

example_statement_1 = """
Les ajustements apportés aux programmes de rémunération et d'avantages sociaux visent à renforcer l’attractivité de l’agence immobilière tout en soutenant ses objectifs de croissance durable.
Ils sont alignés sur la stratégie globale de fidélisation des talents et d’optimisation des coûts. 
Des indicateurs comptables sont suivis mensuellement, et des enquêtes internes mesurent l’évolution de la satisfaction des employés.
"""  # noqa: E501

example_output_1 = """
[
        {{
            "raison": "Vrai. La réponse répond en tout point à la question.",
            "label": "1",
        }}
]
"""  # noqa: E501

example_statement_2 = """
L’agence immobilière a récemment modernisé ses outils numériques pour améliorer l’expérience client et faciliter le travail des agents sur le terrain.
Cette démarche vise à renforcer son image de marque et à mieux répondre aux attentes du marché. 
Des formations ont également été proposées aux collaborateurs pour accompagner cette transformation digitale.
"""  # noqa: E501

example_output_2 = """
[
        {{
            "raison": "Faux. La réponse est partiellement hors sujet en évoquant 'la modernisation de ses outils numériques pour améliorer l’expérience client', ce qui ne répond directement à la question.",
            "label": "0",
        }}
]
"""  # noqa: E501

example_statement_3 = """
L’agence prévoit d’ouvrir de nouvelles succursales en région Auvergne-Rhône-Alpes d’ici la fin de l’année.
Elle a également conclu un partenariat avec une école de commerce pour promouvoir ses métiers auprès des jeunes diplômés.
Une campagne marketing sera lancée au printemps pour soutenir ces initiatives.
"""  # noqa: E501

example_output_3 = """
[
        {{
            "raison": "Faux. L'ensemble de la réponse est hors sujet'.",
            "label": "0",
        }}
]
"""  # noqa: E501

prompt_template = f"""
    ### **Rôle du LLM Juge** :
    Votre mission est d’évaluer la **pertinence** d’une réponse par rapport à une question posée. Une réponse est dite **pertinente** si elle :
    - répond à la question posée,
    - n'introduit pas d'éléments hors sujet,

    Il ne s’agit pas ici d’évaluer la véracité de la réponse, ni son objectivité.


    ### Les données qui vous seront fournies sont :
    - **Question** : La question posée.
    - **Réponse** : La réponse à évaluer.


    ### **Instructions d’évaluation** :
    Adoptez l'approche suivante dans votre évaluation :
        - Lire attentivement la **question**.
        - Lire attentivement la **réponse**.
        - Pour chaque réponse verbalisez un raisonnement pas à pas sur le caractère pertinent des informations de la réponse.
        - En déduire une évaluation finale pour la réponse.
        - Chaque évaluation est un label :
            - Soit 2 : La réponse est totalement pertinente.
            - Soit 1 : La réponse est partiellement pertinente et contient au moins un hors sujet.
            - Soit 0 : La réponse est complètement hors sujet.


    ### **Format de la réponse attendue** :
    Vous devez renvoyer uniquement un JSON dans la structure suivante :
    {json_schema}

    Important : Le contenu renvoyé doit être un JSON strictement valide, sans texte supplémentaire, sans explication ni commentaire, directement parsable et la clé « verdicts » devant correspondre à une liste d'objets JSON.

    ### **Exemples** :
    Voici un ensemble d'exemples de phrases et de leurs évaluations.

    **Exemple 1**
    Exemple de question:
    {example_question}
    Exemple de réponse:
    {example_statement_1}
    Exemple JSON:
    {example_output_1}

    **Exemple 2**
    Exemple de question:
    {example_question}
    Exemple de réponse:
    {example_statement_2}
    Exemple JSON:
    {example_output_2}

    **Exemple 3**
    Exemple de question:
    {example_question}
    Exemple de réponse:
    {example_statement_3}
    Exemple JSON:
    {example_output_3}

    Voici les données :
    Question :
    {{question_fr}}
    Réponse :
    {{answer}}
    JSON:
    """  # noqa: E501
