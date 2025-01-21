import pandas as pd

routes = pd.read_csv("routes.csv")


routes = routes[['Source airport','Destination airport']]
routes = routes.head(100)

print(routes)