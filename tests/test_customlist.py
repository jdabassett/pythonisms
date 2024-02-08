import pytest

from module.customlist import CustomList

assert (pytest and CustomList), "one or more modules not successfully imported: test_custom_list.py file"


# @pytest.mark.skip()
def test_custom_list_exists():
    assert CustomList


# @pytest.mark.skip()
def test_len(create_custom_list):
    new_list = create_custom_list
    assert len(new_list) == 3
    assert isinstance(len(new_list),int)


# @pytest.mark.skip()
def test_dunder_str(create_custom_list):
    assert str(create_custom_list) == "[1,2,3]"


# @pytest.mark.skip()
def test_dunder_repr(create_custom_list):
    assert repr(create_custom_list) == "[1, 2, 3]"


# @pytest.mark.skip()
def test_dunder_getitem(create_custom_list):
    assert create_custom_list[0] == 1
    assert create_custom_list[0:2] == [1,2]
    assert create_custom_list[::] == [1,2,3]
    assert create_custom_list[::-1] == [3,2,1]
    assert create_custom_list[-1] == 3

    with pytest.raises(IndexError):
        value = create_custom_list[5]


# @pytest.mark.skip()
def test_dunder_delitem(create_custom_list):
    new_list = create_custom_list
    del new_list[1]
    assert new_list == [1,3]

    with pytest.raises(IndexError):
        del new_list[10]


# @pytest.mark.skip()
def test_dunder_setitem(create_custom_list):
    new_list = create_custom_list
    new_list[1] = 200
    assert new_list == [1,200,3]
    new_list[::] = [1,2,3]
    assert new_list == [1,2,3]


# @pytest.mark.skip()
def test_dunder_add(create_custom_list):
    new_list = create_custom_list
    new_list += new_list
    assert new_list == [1,2,3,1,2,3]
    new_list += [1,2,3]
    assert new_list == [1,2,3,1,2,3,1,2,3]


# @pytest.mark.skip()
def test_append(create_custom_list):
    new_list = create_custom_list
    new_list.append(4)
    assert new_list == [1,2,3,4]

    with pytest.raises(TypeError):
        new_list.append([1,2,3])


# @pytest.mark.skip()
def test_extend(create_custom_list):
    new_list = create_custom_list
    new_list.extend(new_list)
    assert new_list == [1,2,3,1,2,3]
    new_list.extend([1,2,3])
    assert new_list == [1,2,3,1,2,3,1,2,3]

    with pytest.raises(TypeError):
        new_list.extend(1)


# @pytest.mark.skip()
def test_reverse(create_custom_list):
    new_list = create_custom_list
    new_list.reverse()
    assert new_list == [3,2,1]


# @pytest.mark.skip()
def test_sort(create_custom_list):
    new_list = create_custom_list
    new_list.sort(reverse=True)
    assert new_list == [3,2,1]
    new_list.sort()
    assert new_list == [1,2,3]
    new_list.sort(func=lambda x: -x)
    assert new_list == [3,2,1]


# @pytest.mark.skip()
def test_count(create_custom_list):
    assert create_custom_list.count(1) == 1
    assert create_custom_list.count(10) == 0
    assert create_custom_list.count("A") == 0


# @pytest.mark.skip()
def test_pop(create_custom_list):
    assert create_custom_list.pop() == 3
    assert create_custom_list.pop() == 2
    assert create_custom_list.pop() == 1

    with pytest.raises(IndexError):
        create_custom_list.pop()


# @pytest.mark.skip()
def test_index(create_custom_list):
    assert create_custom_list.index(1) == 0
    assert create_custom_list.index(2) == 1
    assert create_custom_list.index(3) == 2
    assert create_custom_list.index(4) == -1


# @pytest.mark.skip()
def test_remove(create_custom_list):
    create_custom_list.remove(1)
    assert create_custom_list == [2,3]
    create_custom_list.remove(3)
    assert create_custom_list == [2]

    with pytest.raises(ValueError):
        create_custom_list.remove(10)


# @pytest.mark.skip()
def test_insert(create_custom_list):
    create_custom_list.insert(0,10)
    create_custom_list.insert(1, 20)
    create_custom_list.insert(2,30)
    assert create_custom_list == [10,20,30]

    with pytest.raises(IndexError):
        create_custom_list.insert(3,40)


# @pytest.mark.skip()
def test_dunder_boolean(create_custom_list):
    assert False == (not create_custom_list)


# @pytest.mark.skip()
def test_dunder_contains(create_custom_list):
    assert 2 in create_custom_list
    assert 22 not in create_custom_list
    assert "A" not in create_custom_list


# @pytest.mark.skip()
def test_dunder_eq(create_custom_list):
    new_list = CustomList(1,2,3)
    assert create_custom_list == new_list
    assert create_custom_list == [1,2,3]
    assert create_custom_list != [2,3]


# @pytest.mark.skip()
def test_clear(create_custom_list):
    create_custom_list.clear()
    assert create_custom_list == []


# @pytest.mark.skip()
def test_generator(create_custom_list):
    new_list = [1,2,3]
    for val in create_custom_list.generator():
        new_list.remove(val)
    assert new_list == []


# @pytest.mark.skip()
def test_dunder_iter(create_custom_list):
    new_list = [1,2,3]
    for val in create_custom_list:
        new_list.remove(val)
    assert new_list == []


@pytest.fixture
def create_custom_list():
    return CustomList(1,2,3)


