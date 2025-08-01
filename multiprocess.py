import multiprocessing
import sys

def create_ana_show():
    '''Функция, выполняемая в отдельном процессе'''

    import cadquery as cq
    from cadquery.vis import show

    result = cq.Workplane("front").box(2, 3, 0.5)  # make a basic prism
    result = (
        result.faces(">Z").workplane().hole(1)
    )  # find the top-most face and make a hole

    show(result)

if __name__ == '__main__':
    p=multiprocessing.Process(target=create_ana_show)
    p.start()

    p.join()

    sys.exit(0)