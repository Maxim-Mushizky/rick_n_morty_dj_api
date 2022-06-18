from django.http import JsonResponse
from .models import CharacterComparison, CSVFile, ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .api_requests import get_character_data_by_name
from . import logics
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


@api_view(['GET'])
def compare_character(request, first_character_id: str, second_character_id: str):
    first_char = get_character_data_by_name(name=first_character_id)
    if not first_char:
        return Response({"error": f"No character by the name {first_character_id}"}, status.HTTP_404_NOT_FOUND)
    second_char = get_character_data_by_name(name=second_character_id)
    if not second_char:
        return Response({"error": f"No character by the name {second_character_id}"}, status.HTTP_404_NOT_FOUND)
    comparison_result = logics.compare_two_characters(first_char, second_char)
    return JsonResponse(CharacterComparison(**comparison_result).dict())


@api_view(['POST'])
def compare_two_character_to_csv(request, first_character_id: str, second_character_id: str):
    first_char = get_character_data_by_name(name=first_character_id)
    if not first_char:
        return Response({"error": f"No character by the name {first_character_id}"}, status.HTTP_404_NOT_FOUND)
    second_char = get_character_data_by_name(name=second_character_id)
    if not second_char:
        return Response({"error": f"No character by the name {second_character_id}"}, status.HTTP_404_NOT_FOUND)
    try:
        csv_file = CSVFile(**request.data)
    except ValidationError:
        return Response({"error": "Cannot create a file with a non csv extension"},
                        status.HTTP_400_BAD_REQUEST)
    df = logics.get_compare_two_characters_df(first_char, second_char, ak=CharacterComparison.get_attributes())
    df.to_csv(csv_file.path)
    return Response({"SUCCESS!": f"The csv file was created in the path {csv_file.path}"}, status.HTTP_201_CREATED)
