from enum import StrEnum, auto
import string
from typing import Any

LocalizationCheckList = list[tuple[str, list[str]]]()

class Loc:        
    class FieldKey(StrEnum):
        Username = auto()

    dict: dict[str, str]
    def LocalizeMessage(self, key: str, values: list[Any] | dict[FieldKey, Any]):
        if isinstance(values, list):
            return self.dict[key].format(*values)
        else:
            return self.dict[key].format_map({val_key.value: val for val_key, val in values.items()})
    
    @staticmethod
    def NewChecks(*loc_strs: str | tuple[str, list[FieldKey]]):
        for loc_str_obj in loc_strs:
            if isinstance(loc_str_obj, tuple):
                check_item = loc_str_obj[0], [key.value for key in loc_str_obj[1]]
                LocalizationCheckList.append(check_item)
            else:
                check_item = loc_str_obj, list[str]()
                LocalizationCheckList.append(check_item)

    def GetMissingData(self) -> list[str]:
        result = list[str]()
        for key, field_keys in LocalizationCheckList:
            loc_str = self.dict.get(key)
            if not loc_str:
                result.append(f"{key} localization missing")
                continue
            missing_fields = set(field_keys)
            for _, field_name, _, _ in string.Formatter().parse(loc_str):
                if field_name not in missing_fields:
                    result.append(f"{key} has unexpected key {field_name}")
                    continue
                missing_fields.discard(field_name)
            for missing_field in missing_fields:
                result.append(f"{key}.{missing_field} localization missing")
        return result
