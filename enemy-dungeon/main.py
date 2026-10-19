import math
import heapq

# ==========================================
# DATA DUNGEON
# 0 = jalan
# 1 = dinding
# ==========================================

DUNGEON = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
]

ENEMY = (0, 0)
PLAYER = (6, 6)
DETECTION_RANGE = 10


# ==========================================
# 1. DETEKSI JARAK
# ==========================================

def distance(a, b):
    """Menghitung jarak Euclidean antara dua posisi."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def is_player_in_range(enemy, player, detection_range):
    """Mengecek apakah player berada dalam radius deteksi enemy."""
    return distance(enemy, player) <= detection_range


# ==========================================
# 2. ALGORITMA A*
# ==========================================

def heuristic(a, b):
    """Manhattan distance sebagai heuristic A*."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(position):
    """Mengambil posisi yang bisa menjadi tetangga."""
    row, col = position

    directions = [
        (-1, 0),  # atas
        (1, 0),   # bawah
        (0, -1),  # kiri
        (0, 1),   # kanan
    ]

    neighbors = []

    for dr, dc in directions:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < len(DUNGEON) and 0 <= nc < len(DUNGEON[0]):
            if DUNGEON[nr][nc] == 0:
                neighbors.append((nr, nc))

    return neighbors


def a_star(start, goal):
    """Mencari jalur terpendek dari start ke goal menggunakan A*."""

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}

    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score[neighbor] = (
                    tentative_g + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_set,
                    (f_score[neighbor], neighbor)
                )

    return None


# ==========================================
# 3. PROGRAM UTAMA
# ==========================================

def main():
    print("=== SIMULASI ENEMY MENGEJAR PLAYER ===")
    print(f"Posisi Enemy  : {ENEMY}")
    print(f"Posisi Player : {PLAYER}")

    current_distance = distance(ENEMY, PLAYER)

    print(f"Jarak Enemy ke Player: {current_distance:.2f}")

    # Tahap deteksi
    if not is_player_in_range(
        ENEMY,
        PLAYER,
        DETECTION_RANGE
    ):
        print("Player berada di luar jangkauan.")
        print("Enemy tetap melakukan patroli.")
        return

    print("Player terdeteksi!")

    # Tahap pathfinding
    path = a_star(ENEMY, PLAYER)

    if path is None:
        print("Tidak ditemukan jalur menuju Player.")
        return

    print("\nJalur yang ditemukan oleh A*:")
    print(" -> ".join(map(str, path)))

    # Tahap movement
    print("\nPergerakan Enemy:")

    for step, position in enumerate(path):
        print(f"Langkah {step}: Enemy bergerak ke {position}")

    print("\nEnemy berhasil mencapai Player!")


if __name__ == "__main__":
    main()
