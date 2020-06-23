# + Architecture Patterns
- Building Architecture For Event-driven, DDD, TDD, BDD Microservices.

+ defining chaos for software engineer :
This is so common that software engineers have their own term for chaos: the Big Ball of Mud anti-pattern.

![](./static/depandency_diagram.png)

    + Encapsulation and Abstractions :
    - The term encapsulation covers two closely related ideas: simplifying behavior and hiding data. In this discussion,
      we’re using the first sense. We encapsulate behavior by identifying a task that needs to be done in our code and
      giving that task to a well-defined object or function. We call that object or function an abstraction.

    import requests
    params = dict(q='Sausages', format='json')
    parsed = requests.get('http://api.duckduckgo.com/',
    params=params).json()
    results = parsed['RelatedTopics'] for r in results:
    if 'Text' in r:
    print(r['FirstURL'] + ' - ' + r['Text'])

    --------------------------------------------------------------------

    import duckduckgo
    for r in duckduckgo.query('Sausages').results:
    print(r.url + ' - ' + r.text)

    ++ this two examples do the same thing but the second one use a higher level of abstration and encapsulation.

    - Encapsulating behavior by using abstractions is a powerful tool for making code more expressive, more testable, and easier to maintain.


