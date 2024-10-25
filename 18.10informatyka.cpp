// 18.10informatyka.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//
//labyrinth 
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <stack>

using namespace std;

char blankSpace{ '.' };
char wall{ '#' };
char start{ 'S' };
char finish{ 'T' };

class File
{
private:
	string filename;
	ifstream file;
public:
	void openFile(string filename)
	{
		file.open(filename);
		if (file.is_open())
		{
			cout << "Plik zostal otwarty" << endl;
		}
		else
		{
			cout << "Plik nie zostal otwarty" << endl;
		}
	}
	void closeFile()
	{
		file.close();
		if (file.is_open())
		{
			cout << "Plik nie zostal zamkniety" << endl;
		}
		else
		{
			cout << "Plik zostal zamkniety" << endl;
		}
	}
	ifstream& getFile()
	{
		return file;
	}
};
class Generate : File 
{
private:
	int size;
	int StartX;
	int EndX;
	vector<vector<char>> labyrinth;

	void initializeLabyrinth() 
	{
		labyrinth.resize(size, vector<char>(size, wall));
	}

	void carvePath(int x, int y) 
	{
		stack<pair<int, int>> stack;
		stack.push({ x, y });
		labyrinth[y][x] = 'z';

		vector<pair<int, int>> directions = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
		while (!stack.empty()) 
		{
			auto current = stack.top();
			int cx = current.first;
			int cy = current.second;
			vector<pair<int, int>> validDirections;

			for (auto direction : directions) 
			{
				int dx = direction.first;
				int dy = direction.second;
				int nx = cx + dx * 2;
				int ny = cy + dy * 2;
				if (nx >= 0 && nx < size && ny >= 0 && ny < size && labyrinth[ny][nx] == wall) 
				{
					validDirections.push_back({ dx, dy });
				}
			}

			if (!validDirections.empty()) 
			{
				auto direction = validDirections[rand() % validDirections.size()];
				int dx = direction.first;
				int dy = direction.second;
				labyrinth[cy + dy][cx + dx] = blankSpace;
				labyrinth[cy + dy * 2][cx + dx * 2] = blankSpace;
				stack.push({ cx + dx * 2, cy + dy * 2 });
			}
			else 
			{
				stack.pop();
			}
		}
	}

public:
	Generate(int size) 
	{
		srand(time(NULL));
		this->size = size;
		this->StartX = (rand() % (size - 1));
		this->EndX = (rand() % (size - 1));
		initializeLabyrinth();
		cout << "StartX: " << StartX << endl;
		cout << "EndX: " << EndX << endl;
	}

	int getSize() 
	{
		return size;
	}

	void generateMap(string filename) 
	{
		srand(time(NULL));
		initializeLabyrinth();
		labyrinth[0][StartX] = start; // Ustawienie punktu startowego
		labyrinth[size - 1][EndX] = finish; // Ustawienie punktu końcowego

		// Carve a complex path
		carvePath(StartX, 0);

		// Sprawdzenie, czy punkt startowy nie został nadpisany
		if (labyrinth[0][StartX] != start) 
		{
			cout << "Punkt startowy został nadpisany!" << endl;
			labyrinth[0][StartX] = start;
		}

		ofstream file;
		file.open(filename);
		if (file.is_open()) 
		{
			for (int i = 0; i < size; i++) 
			{
				for (int j = 0; j < size; j++) 
				{
					file << labyrinth[i][j];
				}
				file << endl;
			}
			file.close();
		}
		else 
		{
			cout << "Plik nie zostal otwarty" << endl;
		}
	}
	void print() const 
	{
		for (const auto& row : labyrinth) 
		{
			for (char cell : row) 
			{
				cout << cell;
			}
			cout << endl;
		}
	}

	const vector<vector<char>>& getLabyrinth() const 
	{
		return labyrinth;
	}
};
class Labyrinth : File
{
private:
	int size;
	char** labyrinth;
public:
	int numberOfSteps{ 0 }; // zmienna do testow
	int startX{ 0 };
	int startY{ 0 };

	Labyrinth(int size) //mapa labiryntu jest kwadratowa
	{
		this->size = size;
		labyrinth = new char* [size];
		for (int i = 0; i < size; i++)
		{
			labyrinth[i] = new char[size];
		}
	}
	~Labyrinth()
	{
		for (int i = 0; i < size; i++)
		{
			delete[] labyrinth[i];
		}
		delete[] labyrinth;
	}
	void loadFromFile(string filename)
	{
		openFile(filename);
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < size; j++)
			{
				getFile() >> labyrinth[i][j];
			}
		}
		closeFile();
	}
	void print()
	{
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < size; j++)
			{
				cout << labyrinth[i][j];
			}
			cout << endl;
		}
	}
	bool findPath(int x, int y) // dzialanie rekurencyjne, preferowane drogi: dol, gora, prawo, lewo
	{
		numberOfSteps++;
		/*print();*/ // do testow po kolei wypisuje kazdy krok
		/*cout << endl;*/
		if (x < 0 || x >= size || y < 0 || y >= size) // sprawdzamy czy nie wychodzimy poza labirynt
		{
			return false;
		}
		if (labyrinth[x][y] == finish) // sprawdzamy czy jest na mecie
		{
			return true;
		}
		if (labyrinth[x][y] == wall || labyrinth[x][y] == 'v') // sprawdzamy czy nie wchodzimy na sciane lub odwiedzone pole
		{
			return false;
		}
		labyrinth[x][y] = 'v'; // oznaczamy pole jako odwiedzone v = visited
		if (findPath(x + 1, y) == true) // idziemy w dol
		{
			return true;
		}
		if (findPath(x - 1, y) == true) // idziemy w w gore
		{
			return true;
		}
		if (findPath(x, y + 1) == true) // idziemy w prawo
		{
			return true;
		}
		if (findPath(x, y - 1) == true) // idziemy w lewo
		{
			return true;
		}
		labyrinth[x][y] = blankSpace; // oznaczamy pole jako nieodwiedzone
		return false;
	}
	void findStart()
	{
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < size; j++)
			{
				if (labyrinth[i][j] == start)
				{
					startX = i;
					startY = j;
					return;
				}
			}
		}
	}
};
int main()
{
	//Labyrinth labyrinth(10);
	//labyrinth.loadFromFile("map.txt");
	//labyrinth.print();
	//labyrinth.findStart();
	//if (labyrinth.findPath(labyrinth.startX, labyrinth.startY) == true)
	//{
	//	cout << "Znaleziono wyjscie" << endl;
	//}
	//else
	//{
	//	cout << "Nie znaleziono wyjscia" << endl;
	//}
	//cout << "Liczba krokow: " << labyrinth.numberOfSteps << endl;

	Generate generate(20);
	generate.generateMap("mapa.txt");
	int sizeOfGeneratedMap = generate.getSize();


	Labyrinth generatedLabyrinth(sizeOfGeneratedMap);
	generatedLabyrinth.loadFromFile("mapa.txt");
	generatedLabyrinth.print();
	generatedLabyrinth.findStart();
	if (generatedLabyrinth.findPath(generatedLabyrinth.startX, generatedLabyrinth.startY) == true)
	{
		cout << "Znaleziono wyjscie" << endl;
	}
	else
	{
		cout << "Nie znaleziono wyjscia" << endl;
	}
	cout << "Liczba krokow: " << generatedLabyrinth.numberOfSteps << endl;

	return 0;
}

// Uruchomienie programu: Ctrl + F5 lub menu Debugowanie > Uruchom bez debugowania
// Debugowanie programu: F5 lub menu Debugowanie > Rozpocznij debugowanie

// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln

