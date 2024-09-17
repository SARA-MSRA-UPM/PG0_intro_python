from src.generators.PointGenerator import PointGenerator

if __name__ == '__main__':
    pointGenerator = PointGenerator()
    for i in range(10):
        print(pointGenerator.random_point())