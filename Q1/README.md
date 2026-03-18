# AI Assignment 3

## Q1 – Dijkstra Algorithm for Indian Cities

This program implements **Dijkstra’s Algorithm (Uniform Cost Search)** to find the shortest road distance between Indian cities.

Cities are represented as **nodes** and road distances are **edge weights**.

The dataset is stored in `india_roads.csv`.

---

## Files in Repository

dijkstra_india.py – Python implementation of Dijkstra's Algorithm  
india_roads.csv – Road distance dataset between major Indian cities

---

## How to Run

```bash
python q1.py

##Example Input
Enter source city: Delhi

##Example Output:

Shortest distances from Delhi 

Delhi : 0 km | Path -> Delhi
Jaipur : 281.0 km | Path -> Delhi -> Jaipur
Chandigarh : 244.0 km | Path -> Delhi -> Chandigarh
Lucknow : 555.0 km | Path -> Delhi -> Lucknow
Agra : 233.0 km | Path -> Delhi -> Agra
Ahmedabad : 938.0 km | Path -> Delhi -> Jaipur -> Ahmedabad
Surat : 1204.0 km | Path -> Delhi -> Jaipur -> Ahmedabad -> Surat
Mumbai : 1488.0 km | Path -> Delhi -> Jaipur -> Ahmedabad -> Surat -> Mumbai
Pune : 1636.0 km | Path -> Delhi -> Jaipur -> Ahmedabad -> Surat -> Mumbai -> Pune
Hyderabad : 1720.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad
Bangalore : 2290.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Bangalore
Chennai : 2350.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Chennai
Kanpur : 645.0 km | Path -> Delhi -> Lucknow -> Kanpur
Varanasi : 975.0 km | Path -> Delhi -> Lucknow -> Kanpur -> Varanasi
Patna : 1235.0 km | Path -> Delhi -> Lucknow -> Kanpur -> Varanasi -> Patna
Kolkata : 1818.0 km | Path -> Delhi -> Lucknow -> Kanpur -> Varanasi -> Patna -> Kolkata
Bhubaneswar : 2259.0 km | Path -> Delhi -> Lucknow -> Kanpur -> Varanasi -> Patna -> Kolkata -> Bhubaneswar
Visakhapatnam : 2340.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Visakhapatnam
Indore : 1057.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Indore
Bhopal : 866.0 km | Path -> Delhi -> Jaipur -> Bhopal
Nagpur : 1218.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur
Raipur : 1503.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Raipur
Ranchi : 1973.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Raipur -> Ranchi
Coimbatore : 2653.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Bangalore -> Coimbatore
Kochi : 2843.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Bangalore -> Coimbatore -> Kochi
Thiruvananthapuram : 3049.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Bangalore -> Coimbatore -> Kochi -> Thiruvananthapuram
Srinagar : 876.0 km | Path -> Delhi -> Srinagar
Amritsar : 473.0 km | Path -> Delhi -> Chandigarh -> Amritsar
Shimla : 357.0 km | Path -> Delhi -> Chandigarh -> Shimla
Guwahati : 2015.0 km | Path -> Delhi -> Lucknow -> Kanpur -> Varanasi -> Patna -> Guwahati
Goa : 2078.0 km | Path -> Delhi -> Jaipur -> Ahmedabad -> Surat -> Mumbai -> Goa
Madurai : 2811.0 km | Path -> Delhi -> Jaipur -> Bhopal -> Nagpur -> Hyderabad -> Chennai -> Madurai
