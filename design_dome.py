# design_dome.py

import math

# 재질별 밀도 (g/cm3)
MATERIAL_DENSITY = {
    "유리": 2.4,
    "알루미늄": 2.7,
    "탄소강": 7.85
}

# 지구 및 화성 중력 (m/s^2)
EARTH_GRAVITY = 9.80665
MARS_GRAVITY = 3.72076

# 전역변수 초기화
calculated_result = {}

def sphere_area(diameter, material="유리", thickness=1):
    """
    완전한 반구 돔의 면적과 무게 계산
    :param diameter: 돔 지름 (m)
    :param material: 재질 (문자열)
    :param thickness: 두께 (cm)
    :return: None
    """

    # 재질 유효성 검사
    if material not in MATERIAL_DENSITY:
        print(f"[경고] 입력한 재질 '{material}'은(는) 지원되지 않습니다. 기본값 '유리'로 설정합니다.")
        material = "유리"

    # 단위 변환
    diameter_cm = diameter * 100          # m → cm
    radius_cm = diameter_cm / 2

    # 반구 면적 계산 (cm²)
    area_cm2 = 2 * math.pi * (radius_cm ** 2)

    # 재질 밀도 (kg/cm3)로 변환
    density_kg_per_cm3 = MATERIAL_DENSITY[material] / 1000

    # 체적 계산 = 면적 × 두께 (cm³)
    volume_cm3 = area_cm2 * thickness

    # 지구 기준 무게 (kg)
    weight_earth = volume_cm3 * density_kg_per_cm3

    # 화성 기준 무게
    weight_mars = weight_earth * (MARS_GRAVITY / EARTH_GRAVITY)

    # 소수점 이하 셋째 자리까지 반올림
    area_cm2 = round(area_cm2, 3)
    weight_mars = round(weight_mars, 3)

    # 전역변수에 저장
    global calculated_result
    calculated_result = {
        "material": material,
        "diameter": diameter,
        "thickness": thickness,
        "area": area_cm2,
        "weight": weight_mars
    }

    # 출력
    print(
        f"재질 =⇒ {material}, "
        f"지름 =⇒ {diameter} m, "
        f"두께 =⇒ {thickness} cm, "
        f"면적 =⇒ {area_cm2} cm², "
        f"무게 =⇒ {weight_mars} kg"
    )


if __name__ == "__main__":
    try:
        # diameter 입력
        while True:
            diameter_input_str = input("돔의 지름을 입력하세요 (m): ").strip()
            if diameter_input_str == "":
                print("[오류] 지름은 필수 입력입니다. 다시 입력하세요.")
                continue
            try:
                diameter_input = float(diameter_input_str)
                if diameter_input <= 0:
                    print("[오류] 지름은 0보다 커야 합니다.")
                    continue
                break
            except ValueError:
                print("[오류] 지름은 숫자로 입력해야 합니다.")
        
        # material 입력
        material_input = input(f"재질을 입력하세요 {list(MATERIAL_DENSITY.keys())} [기본값: 유리]: ").strip()
        if material_input == "":
            material_input = "유리"
        else:
            # 숫자 잘못 입력 방지
            try:
                float(material_input)
                print("[오류] 재질은 문자를 입력해야 합니다. 다시 기본값 '유리'로 설정합니다.")
                material_input = "유리"
            except ValueError:
                if material_input not in MATERIAL_DENSITY:
                    print(f"[경고] 입력한 재질 '{material_input}'은(는) 지원되지 않습니다. 기본값 '유리'로 설정합니다.")
                    material_input = "유리"

        # thickness 입력
        thickness_input_str = input("두께를 입력하세요 (cm) [기본값: 1]: ").strip()
        if thickness_input_str == "":
            thickness_input = 1
        else:
            try:
                thickness_input = float(thickness_input_str)
                if thickness_input <= 0:
                    print("[오류] 두께는 0보다 커야 합니다. 기본값 1 cm로 설정합니다.")
                    thickness_input = 1
            except ValueError:
                print("[오류] 두께는 숫자로 입력해야 합니다. 기본값 1 cm로 설정합니다.")
                thickness_input = 1

        sphere_area(
            diameter=diameter_input,
            material=material_input,
            thickness=thickness_input
        )

    except Exception as e:
        print(f"[오류] 예기치 못한 오류가 발생했습니다: {e}")
