import sys
import os
import shutil


def gen(base=sys.argv[1], project=sys.argv[2]):
    """
    Create project template with various sub-folders and files.

    :param base: Folder where main project folder will be created.
    :type base: string (put in quotes if file path contains spaces).
    :param project: Name of project; this will be used to generate the main folder.
    :type project: string (put in quotes if project name contains spaces).
    :return: None
    """
    folders = (os.path.join(base, project),
               os.path.join(base, project, 'src'),
               os.path.join(base, project, 'src', 'code'),
               os.path.join(base, project, 'data'),
               os.path.join(base, project, 'data', 'raw'),
               os.path.join(base, project, 'data', 'proc'),
               os.path.join(base, project, 'doc'),
               os.path.join(base, project, 'doc', 'notes'),
               os.path.join(base, project, 'doc', 'ethics'),
               os.path.join(base, project, 'doc', 'ethics', 'scans'),
               os.path.join(base, project, 'doc', 'ms'),
               os.path.join(base, project, 'doc', 'slides'),
               os.path.join(base, project, 'doc', 'protocol'),
               os.path.join(base, project, 'doc', 'results'),
               os.path.join(base, project, 'doc', 'misc'))

    for path in folders:
        try:
            os.mkdir(path)
        except FileExistsError:
            print('\nThe folder {} already exists. Please delete the project folder '
                  'and re-run this function if you truly want to create a blank template '
                  'project folder named "{}".\n'.format(path, project))
            sys.exit(1)  # abort
    # Copy over folder and associated files for ms and notes LaTex documents
    shutil.copytree('./ms_md', os.path.join(base, project, 'src', 'ms_md'))
    # shutil.copytree('./ms_tex', os.path.join(base, project, 'src', 'ms_tex'))
    shutil.copytree('./notes_md', os.path.join(base, project, 'src', 'notes_md'))
    # shutil.copytree('./notes_tex', os.path.join(base, project, 'src', 'notes_tex'))
    shutil.copytree('./protocol_md', os.path.join(base, project, 'src', 'protocol_md'))
    # shutil.copytree('./protocol_tex', os.path.join(base, project, 'src', 'protocol_tex'))
    shutil.copytree('./slides_md', os.path.join(base, project, 'src', 'slides_md'))
    # shutil.copytree('./slides_tex', os.path.join(base, project, 'src', 'slides_tex'))
    shutil.copytree('./<project>', os.path.join(base, project, 'src', 'code', '<project>'))
    shutil.copytree('./tests', os.path.join(base, project, 'src', 'code', 'tests'))
    shutil.copy('./setup_init/README.md', os.path.join(base, project))
    shutil.copy('./setup_repo/README.md', os.path.join(base, project, 'src', 'code'))
    shutil.copy('./setup_repo/make_venv.sh', os.path.join(base, project, 'src', 'code'))
    shutil.copy('./setup_repo/requirements.txt', os.path.join(base, project, 'src', 'code'))
    shutil.copy('./setup_repo/LICENSE.md', os.path.join(base, project, 'src', 'code'))
    shutil.copy('./.gitignore', os.path.join(base, project))

if __name__ == '__main__':
    gen()
