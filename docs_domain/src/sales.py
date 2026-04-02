# TODO refactor this module using business logic names

from typing import List, Dict, Optional, Any


def _row(x: str) -> Optional[Dict[str, Any]]:
    """Parse one line from file into a dictionary."""
    # x is one line from file
    p = x.strip().split(",")  # split by comma
    if len(p) != 4:  # if line is bad
        return None  # return nothing

    name = p[0]  # product name
    category = p[1]  # product category
    price = float(p[2])  # price of one item
    quantity = int(p[3])  # amount of items

    return {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
    }  # make dict with business logic names


def read_data(path: str) -> List[Dict[str, Any]]:
    """Read and parse data from CSV file."""
    res = []  # final list
    with open(path, "r", encoding="utf-8") as f:  # open file
        for x in f:  # go over lines
            r = _row(x)  # convert line to dict
            if r is not None:  # if parsing was ok
                res.append(r)  # add to result
    return res  # return result


def total(ds: List[Dict[str, Any]], d: float = 0) -> float:
    """Calculate total sum with optional discount percentage."""
    s = 0  # total sum
    for item in ds:  # loop all rows
        s = s + item["price"] * item["quantity"]  # add price * quantity
    if d:  # if discount exists
        s = s - s * d / 100  # apply discount
    return s  # give answer


def find_big(ds: List[Dict[str, Any]], t: float) -> List[Dict[str, Any]]:
    """Find rows where total value is >= threshold."""
    out = []  # rows that are big enough
    for item in ds:  # each row
        x = item["price"] * item["quantity"]  # row money
        if x >= t:  # compare with threshold
            out.append(item)  # save row
    return out  # done


def by_category(ds: List[Dict[str, Any]]) -> Dict[str, float]:
    """Group total amounts by category."""
    m = {}  # category to money
    for item in ds:  # each row
        k = item["category"]  # category name
        if k not in m:  # create if needed
            m[k] = 0  # start from zero
        m[k] += item["price"] * item["quantity"]  # add row amount
    return m  # return mapping


def report(ds: List[Dict[str, Any]]) -> str:
    """Generate a formatted report."""
    lines = []  # text lines
    lines.append("Report")  # title
    lines.append("------")  # separator

    for k, v in by_category(ds).items():  # category and amount
        lines.append(f"{k}: {v}")  # make line

    lines.append("------")  # separator again
    lines.append(f"Total: {total(ds)}")  # total sum

    return "\n".join(lines)  # merge lines


def write_report(path: str, txt: str) -> None:
    # TODO better errors
    with open(path, "w", encoding="utf-8") as f:  # open file for writing
        f.write(txt)  # write text