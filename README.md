# GPS Distance

# Install

```bash
$ pip install gpsdistance
```

## Usage


```python
import gpsdistance
```

# Two-dimensional Distance (kilometer based)

```python
dist = gpsdistance.gpsdistance()

print(dist.get_2distance(lat1, lon1, lat2, lon2))
```


# three-dimensional Distance (kilometer based)

```python
dist = gpsdistance.gpsdistance()

print(dist.get_3distance(lat1, lon1, alt1, lat2, lon2, alt2))
```

